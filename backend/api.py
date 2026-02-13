from fastapi import FastAPI, HTTPException,Depends
from pydantic import BaseModel
from datetime import datetime, timedelta
import psycopg2
from fastapi.middleware.cors import CORSMiddleware
from db_pg import get_pg_connection
from fastapi import HTTPException, Depends
from security import get_password_hash, verify_password, create_access_token, create_refresh_token, verify_token

# python -m uvicorn api:app --reload
# http://127.0.0.1:8000/docs#

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ======================
# APP
# ======================



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
def realtime_api(data: UserAccount):
    # JOIN ที่ PostgreSQL
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
    # print(access_token)
    # refresh_token = create_refresh_token(data={"sub": email, "type": "refresh"})
    
    # ส่ง Token กลับไปให้ลูกค้า
    return {
        "access_token": access_token, 
        # "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@app.get("/getdata")
# def get_all_sensor_data():
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

    return {
        "message": "Register success",
        "status_code": "200"
    }
    
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
    