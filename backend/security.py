from datetime import datetime, timedelta
from typing import Optional
from jose import jwt,JWTError # ไลบรารีสำหรับจัดการ JWT (JSON Web Token)
from passlib.context import CryptContext # ไลบรารีสำหรับ Hash Password
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

# --- ส่วนของการตั้งค่า (Configuration) ---

# SECRET_KEY: กุญแจลับที่ใช้เซ็น Digital Signature ให้กับ Token 
# run code => "python -c "import secrets; print(secrets.token_hex(32))"
# *สำคัญมาก* ในงานจริงห้ามเขียนใส่ Code แบบนี้ ควรเก็บใน Environment Variable เพื่อความปลอดภัย
# ถ้าคนอื่นรู้ key นี้ เขาจะสามารถปลอมแปลง Token เป็นใครก็ได้ในระบบเรา
SECRET_KEY = "d14d3ec700478ec6ed14fc66249c3da9885e2d00bef155c05ef293339c8dbe45" 

# ALGORITHM: อัลกอริทึมที่ใช้เข้ารหัส (HS256 เป็นแบบ Symmetric Key ที่นิยมใช้)
ALGORITHM = "HS256"

# ACCESS_TOKEN_EXPIRE_MINUTES: อายุของ Token (นาที) หลังจากนี้ Token จะใช้ไม่ได้ ต้อง Login ใหม่
ACCESS_TOKEN_EXPIRE_second = 60
REFRESH_TOKEN_EXPIRE_MINUTES = 30

# --- ส่วนของการจัดการ Password ---

# ตั้งค่า Context สำหรับการ Hash รหัสผ่าน
# schemes=["bcrypt"]: เลือกใช้อัลกอริทึม bcrypt ซึ่งปลอดภัยและนิยมมากสำหรับการเก็บรหัสผ่าน
# deprecated="auto": รองรับการอัปเดตอัลกอริทึมในอนาคตอัตโนมัติ (Backward Compatibility)
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_password(plain_password, hashed_password):
    """
    ฟังก์ชันตรวจสอบรหัสผ่าน (ใช้ตอน Login)
    รับค่า:
      - plain_password: รหัสผ่านดิบที่ User กรอกมา (เช่น '1234')
      - hashed_password: รหัสที่ Hash แล้วจาก Database (เช่น '$2b$...')
    คืนค่า: True ถ้าตรงกัน, False ถ้าไม่ตรง
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """
    ฟังก์ชันแปลงรหัสผ่านเป็น Hash (ใช้ตอน Register หรือเปลี่ยนรหัส)
    รับค่า: รหัสผ่านดิบ
    คืนค่า: String ที่ถูก Hash แล้ว (เอาไปเก็บลง DB)
    """
    return pwd_context.hash(password)

# --- ส่วนของการจัดการ Token (JWT) ---

def create_access_token(data: dict):
    """
    ฟังก์ชันสร้าง JWT Token (ใช้ตอน Login สำเร็จ เพื่อแจกบัตรผ่าน)
    รับค่า: data (Dictionary ข้อมูลที่จะฝังลงใน Token เช่น {'sub': 'user1'})
    """
    # สำเนาข้อมูลเพื่อไม่ให้กระทบกับ dict ต้นฉบับ
    to_encode = data.copy()
    
    # คำนวณเวลาหมดอายุ (เวลาปัจจุบัน + 30 นาที)
    # utcnow() ใช้เวลามาตรฐานโลกเพื่อป้องกันปัญหาเรื่อง Timezone
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_second)
    
    # เพิ่ม field 'exp' (expiration) เข้าไปในข้อมูล Token
    # JWT มาตรฐานจะเช็ค field นี้ให้อัตโนมัติว่าหมดอายุหรือยัง
    to_encode.update({"exp": expire})
    
    # ทำการ Encode (สร้าง Token)
    # ใช้ SECRET_KEY และ ALGORITHM ที่ตั้งไว้ข้างบนในการเซ็นกำกับ
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt

def create_refresh_token(data: dict):
    """
    ฟังก์ชันสร้าง JWT Token (ใช้ตอน Login สำเร็จ เพื่อแจกบัตรผ่าน)
    รับค่า: data (Dictionary ข้อมูลที่จะฝังลงใน Token เช่น {'sub': 'user1'})
    """
    # สำเนาข้อมูลเพื่อไม่ให้กระทบกับ dict ต้นฉบับ
    to_encode = data.copy()
    
    # คำนวณเวลาหมดอายุ (เวลาปัจจุบัน + 30 นาที)
    # utcnow() ใช้เวลามาตรฐานโลกเพื่อป้องกันปัญหาเรื่อง Timezone
    expire = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
    # เพิ่ม field 'exp' (expiration) เข้าไปในข้อมูล Token
    # JWT มาตรฐานจะเช็ค field นี้ให้อัตโนมัติว่าหมดอายุหรือยัง
    data.update({"exp": expire})
    
    # ทำการ Encode (สร้าง Token)
    # ใช้ SECRET_KEY และ ALGORITHM ที่ตั้งไว้ข้างบนในการเซ็นกำกับ
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt


# def create_token(username: str):
#     return create_access_token(
#         {"sub": username, "type": "refresh"},
#         timedelta(seconds=ACCESS_TOKEN_EXPIRE_second)
#     )

# def refresh_token(username: str):
#     return create_refresh_token({"sub": username, "type": "refresh"},
#         timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
#     )

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: int | None = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload",
            )

        return username

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )
