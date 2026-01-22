from fastapi import APIRouter, Depends
from dto.dto_user import InputUser

router_user = APIRouter(prefix="/api/v1")

@router_user.post('/user')
def register_user(inputUser : InputUser) : 
    