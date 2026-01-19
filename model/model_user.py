from pydantic.v1 import BaseModel, Field 
from model.model_common import PyObjectId

class UserTransaction(BaseModel) : 
    id : PyObjectId = Field(alias='_id')
    username : str
    password : 
    class Config : 
        json_encoders = {ObjectId : str}