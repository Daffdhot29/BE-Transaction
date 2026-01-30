from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated
from fastapi import Depends, HTTPException, status
from dto.dto_common import tokenData
from service.service_jwt import serviceJwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], service_jwt : serviceJwt = Depends()):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    
    