import jwt
from datetime import datetime, timedelta
from config import AppConfig
SECRET_KEY = AppConfig.JWT_SECRECT
ALGORITHM = AppConfig.ALGORITHM

def creare_token(payload, expires_delta):
    to_encode = payload.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt