from fastapi import APIRouter, Depends, HTTPException
from dto.dto_user import InputUser, InputLogin
from service.service_user import ServiceUser


router_user = APIRouter(prefix="/api/v1", tags=["User"])

@router_user.post('/user')
def register_user(inputUser : InputUser, service_user : ServiceUser = Depends()) : 
    service_user.insert_new_user(inputUser)
    return inputUser 

@router_user.post('/login')
def login_user(inputLogin : InputLogin, service_user : ServiceUser = Depends()) : 
    user = service_user.login_user(inputLogin)
    if user is None : 
        if inputLogin.username is None : 
            raise HTTPException(status_code=400, detail="Username is required")
        if inputLogin.password is None : 
            raise HTTPException(status_code=400, detail="Password is required")
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return user 