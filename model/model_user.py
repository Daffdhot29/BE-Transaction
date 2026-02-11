from pydantic.v1 import BaseModel, Field 
from model.model_common import PyObjectId
from bson import ObjectId

class UserTransaction(BaseModel) : 
    id : PyObjectId = Field(alias='_id')
    username : str
    password : str
    name : str
    
    class Config : 
        json_encoders = {ObjectId : str}