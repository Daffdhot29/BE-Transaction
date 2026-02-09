from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from typing import Union
from fastapi import HTTPException
from dto.dto_common import tokenData
from jwt.exceptions import InvalidTokenError

class serviceJwt : 
    # inisialisasi variabel
    def __init__(self)-> None :
        self.SECRET_KEY  = "e9950a48d4e69d360bc5bbf0f1c9b0cc5799d28b24248dcaeea3c9f82544a747"
        self.ALGORITHM = "HS256"
        self.ACCESS_TOKEN_EXPIRE_MINUTES = 30

    # membuat token akses
    def create_access_token(self, data:dict, expire_delta: timedelta | None = None): 
        to_encode = data.copy()
        if expire_delta : 
            expire = datetime.now(timezone.utc) + expire_delta
        else : 
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp" : expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt
    
    def decode_token(self, token:str) : 
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            return payload 
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid Credential")
