from pydantic.v1 import BaseModel

class InputUser(BaseModel) : 
    username : str 
    password : str
    name : str
    