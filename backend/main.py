from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
# import create_access_token เพิ่มเข้ามา
from security import get_password_hash, verify_password, create_access_token, verify_token

app = FastAPI()

# จำลอง Database
fake_users_db = {}
access_token = {}

class User(BaseModel):
    username: str
    password: str
    

class UserInfo(BaseModel):
    username: str
    password: str
    
@app.get("/")
def showdata():
    return fake_users_db

@app.post("/register")
def register(user: User):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = get_password_hash(user.password)
    
    fake_users_db[user.username] = {
        "username": user.username,
        "hashed_password": hashed_password
    }
    return {"message": "User created successfully"}

@app.post("/login")
def login(user: User):
    user_in_db = fake_users_db.get(user.username)
    if not user_in_db:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    stored_hash = user_in_db["hashed_password"]
    
    # ถ้า Verify ผ่าน
    if not verify_password(user.password, stored_hash):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    # *** จุดเปลี่ยน: สร้าง Token ***
    # ใส่ข้อมูล user.username เข้าไปใน token (เรียกว่า sub หรือ subject)
    access_token = create_access_token(data={"sub": user.username})
    print(access_token)
    
    # ส่ง Token กลับไปให้ลูกค้า
    return {
        "access_token": access_token, 
        "token_type": "bearer"
    }
    
@app.get("/me", response_model=UserInfo)
def read_me(user_id: int = Depends(verify_token)):
    user = fake_users_db.get(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
    