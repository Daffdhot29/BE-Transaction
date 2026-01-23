from pydantic.v1 import BaseModel 

class ResponseMessage(BaseModel) : 
    detail : str