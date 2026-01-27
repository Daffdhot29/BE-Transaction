from fastapi import APIRouter, Depends, HTTPException
from typing_extensions import Annotated 
from fastapi.security import OAuth2PasswordRequestForm

from dto.dto_user import InputUser, InputLogin, OutputLogin
from dto.dto_common import ResponseMessage
from service.service_user import ServiceUser


router_user = APIRouter(prefix="/api/v1", tags=["User"])

@router_user.post('/user')
def register_user(inputUser : InputUser, service_user : ServiceUser = Depends()) : 
    service_user.insert_new_user(inputUser)
    return ResponseMessage(detail="User Register Successful")

@router_user.post('/login', response_model=OutputLogin)
def login_user(
    formData : Annotated[OAuth2PasswordRequestForm, Depends()], 
    service_user : ServiceUser = Depends()) :
    # Konversi form data OAuth2 ke InputLogin DTO
    login = InputLogin(
            username=formData.username,
            password=formData.password
    ) 
    # Panggil service login
    # if user is None : 
    #     raise HTTPException(status_code=401, detail="Invalid username or password")
    # return ResponseMessage(detail="Login Successful")

    jwt_token = service_user.login_user(
        login
    )

    return OutputLogin(token=jwt_token)