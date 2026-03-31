import asyncio
from typing import List
from fastapi import FastAPI, HTTPException,Depends, Response,  WebSocket, Request, Cookie, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from db_pg import get_pg_connection
from security import get_password_hash, verify_password, create_access_token, verify_token
from dotenv import load_dotenv
from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import RedirectResponse
from influxdb import InfluxDBClient
import os
import json

# python -m uvicorn api:app --reload
# http://127.0.0.1:8000/docs#

load_dotenv()
connected_clients = []

app = FastAPI()

# list ของ URL ที่ “อนุญาต” ให้มาเรียก API ของเราได้
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5500",
]

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

INFLUX_HOST = os.getenv("INFLUX_HOST")
INFLUX_PORT = os.getenv("INFLUX_PORT")
INFLUX_DB = os.getenv("INFLUX_DB")

# ======================
# GOOGLE
# ======================
client_id=os.getenv("GOOGLE_CLIENT_ID")
client_secret=os.getenv("GOOGLE_CLIENT_SECRET")

#จำ user โดยเก็บ cookie ไว้ เวลาเข้ามาใหม่ก็จะรู้ว่าคนนี้เคยเข้ามาก่อนแล้ว
app.add_middleware(SessionMiddleware, secret_key="supersecret")

oauth = OAuth()

oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"}
)


# POSTGRES CONNECTION
conn = get_pg_connection()
cur = conn.cursor()

# ======================
class UserInfo(BaseModel):
    username: str
    password: str
    
class UserCreate(BaseModel):
    username: str
    password: str
    name: str
    surname: str
    email: str
    
class UserAccount(BaseModel):
    email: str
    password: str    
    
class TokenData(BaseModel):
    username: str 

# ======================
# API ENDPOINT
# ======================

@app.post("/login")
def realtime_api(data: UserAccount, response: Response):
    # JOIN ที่ PostgreSQL
    try: 
        cur.execute("""
            SELECT d.user_id,
                d.username,
                d.password,
                d.hashed_password,
                df.name,
                df.surname,
                df.email
            FROM account d
            JOIN profile df
                ON d.user_id = df.id
            WHERE df.email = %s
                and d.password = %s;
        """, (data.email,data.password,))
        
    except: 
        return("failed database connecting")

    rows = cur.fetchall()

    if not rows:
        # raise HTTPException(
        #     status_code=200,
        #     detail="Incorrect username or password"
        # )
        return {
            "status_code": 200,
            "detail": "Incorrect username or password"
        }

    hashed_password = rows[0][3]
    email = rows[0][6]
    
    stored_hash = hashed_password
    
    # ถ้า Verify ผ่าน
    if not verify_password(data.password, stored_hash):
        return {
            "status_code": 200,
            "detail": "Incorrect username or password"
        }
    
    # *** จุดเปลี่ยน: สร้าง Token ***
    # ใส่ข้อมูล user.username เข้าไปใน token (เรียกว่า sub หรือ subject)
    access_token = create_access_token(data={"sub": email, "type": "access"})
    # refresh_token = create_refresh_token(data={"sub": email, "type": "refresh"})
    
    # ส่ง Token กลับไปให้ลูกค้า
    # return {
    #     "access_token": access_token, 
    #     # "refresh_token": refresh_token,
    #     "token_type": "bearer"
    # }
    
    # เอา access token ไปเก็บใน cookie
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,      # localhost ต้อง False
        samesite="lax"
    )

    return {
        "message": "Login successful"
    }
    
@app.post("/logout")
def logout(response: Response):
    response.delete_cookie(
        key="access_token",
        httponly=True,
        secure=False,      # localhost ต้อง False
        samesite="lax"
    )
    return {"message": "Logged out successfully"}

@app.get("/getdata")
def read_me(email: str = Depends(verify_token)):
    conn = get_pg_connection()
    cur = conn.cursor()    

    cur.execute("""
        SELECT d.user_id,
               d.username,
               df.name,
               df.surname,
               df.email
        FROM account d
        JOIN profile df
            ON d.user_id = df.id
            where df.email = %s
    """, (email,))
    
    rows = cur.fetchall()

    cur.close()
    conn.close()
    
    return [
        {
            "name": r[2],
            "surname": r[3],
            "email": r[4]
        }
        for r in rows
    ]
    
@app.post("/register")
def register_user(data: UserCreate):
    conn = get_pg_connection()
    cur = conn.cursor()
    
    cur.execute("""SELECT email
                FROM profile
                where email = %s;
    """, (data.email,))
    
    rows = cur.fetchone()
    
    # username = rows[0]
    if rows is not None:
        # return {
        #     "message": "Email already registered",
        #     "status_code": "400"
        # }
        raise HTTPException(
        status_code=400,
        detail="Email already registered"
    )
        
    hashed_password = get_password_hash(data.password)

    cur.execute("""
        INSERT INTO account (username, password, hashed_password)
        VALUES (%s, %s, %s)
        RETURNING user_id;
    """, (data.username, data.password, hashed_password,))
    
    # insert profile
    cur.execute("""
        INSERT INTO profile (name, surname, email)
        VALUES (%s, %s, %s)
        RETURNING id
       ;
    """, ( data.name, data.surname, data.email))

    conn.commit()
    
    jwt_token = create_access_token(
        data={"sub": data["email"], "type": "access"}
    )
    
    response = RedirectResponse(
        url="http://localhost:5173/homepage"
    )
    
    response.set_cookie(
        key="access_token",
        value=jwt_token,
        httponly=True,
        secure=False,  # dev
        samesite="lax"
    )

    return {
        "message": "Register success",
        "status_code": "200"
    }
    
@app.get("/auth/google")
async def login_google(request: Request):
    redirect_uri = request.url_for("auth_callback")
    return await oauth.google.authorize_redirect(request, redirect_uri)

@app.get("/auth/google/callback")
async def auth_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user = token.get("userinfo")

    google_user_data = {
        "email": user.get("email"),
        "first_name": user.get("given_name"),
        "last_name": user.get("family_name")
    }

    conn = get_pg_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT email FROM profile
        WHERE email = %s
    """, (google_user_data["email"],))

    existing_user = cur.fetchone()

    cur.close()
    conn.close()

    # ✅ ถ้ามี user แล้ว → login ปกติ
    if existing_user:
        jwt_token = create_access_token(
            data={"sub": google_user_data["email"], "type": "access"}
        )

        response = RedirectResponse(
            url="http://localhost:5173/homepage"
        )

        response.set_cookie(
            key="access_token",
            value=jwt_token,
            httponly=True,
            secure=False,  # dev
            samesite="lax"
        )

        return response

    # ✅ ถ้ายังไม่มี user → เก็บ email ไว้ใน cookie แทน query
    response = RedirectResponse(
        url="http://localhost:5173/register"
    )

    # response.set_cookie(
    #     key="google_user",
    #     value=json.dumps(google_user_data),
    #     httponly=True,
    #     secure=False,
    #     samesite="lax"
    # )

    return response

@app.get("/google-user")
def get_google_user(google_user: str = Cookie(None)):
    # if not google_user:
    #     raise HTTPException(status_code=401, detail="No Google user found")

    try:
        user_data = json.loads(google_user)
    except:
        raise HTTPException(status_code=400, detail="Invalid cookie format")

    return user_data
    
@app.post("/refresh")
def refresh_token(refresh_token: str):
    username = verify_token(refresh_token)
    # read_me(username: str = Depends(verify_token)):

    # username = payload["sub"]
    new_access_token = create_access_token(data={"sub": username, "type": "access"})
    # new_refresh_token = create_refresh_token(data={"sub": username, "type": "refresh"})
    
    return {
        "access_token": new_access_token,
        # "refresh_token": new_refresh_token
    }
  
@app.websocket("/ws/dashboard")
async def websocket_dashboard(websocket: WebSocket, access_token: str = Cookie(None)):
# async def websocket_dashboard(websocket: WebSocket):
    if not access_token:
        await websocket.close(code=1008)
        return

    # verify JWT
    user = verify_token(access_token)
    if not user:
        await websocket.close(code=1008)
        return
    
    await websocket.accept()

    client = InfluxDBClient(
        host=INFLUX_HOST,
        port=int(INFLUX_PORT),
        database=INFLUX_DB
    )

    while True:
        print("Loop running...")
        
        query = '''
            SELECT LAST("battery") AS battery,
                   LAST("motor") AS motor,
                   LAST("sonar") AS sonar,
                   LAST("signal") AS signal
            FROM "MFEC"
        '''

        result = client.query(query)
        points = list(result.get_points())
        
        print("POINTS:", points)

        if points:
            await websocket.send_json(points[0])

        await asyncio.sleep(5)  # ดึงทุก 2 วิ
        
@app.get("/api/dashboard/latest")
async def get_latest_records(limit: int = 20):
    client = InfluxDBClient(
        host=INFLUX_HOST,
        port=int(INFLUX_PORT),
        database=INFLUX_DB
    )

    query = f'''
        SELECT "battery", "motor", "sonar", "signal"
        FROM "MFEC"
        ORDER BY time DESC
        LIMIT {limit}
    '''

    result = client.query(query)
    points = list(result.get_points())

    # reverse ให้เรียงเก่า → ใหม่
    points.reverse()

    return points