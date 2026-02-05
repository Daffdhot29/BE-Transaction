from pydantic.v1 import BaseModel 

class ResponseMessage(BaseModel) : 
    detail : str

class tokenData(BaseModel) : 
    userId : str
    name : str

class pageBase(BaseModel) : 
    page : int
    size : int 
    totalData : int 
    totalPage : int 