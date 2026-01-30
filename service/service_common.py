from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated
from fastapi import Depends
from dto.dto_common import tokenData
from service.service_jwt import serviceJwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], service_jwt : serviceJwt = Depends()):
    current_token = tokenData.parse_obj( service_jwt.decode_token(token))
    return current_token   
    
    