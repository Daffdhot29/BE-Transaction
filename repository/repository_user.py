from fastapi import Depends 
from pymongo.database import Database 
from config.config import get_db_connection 
from dto.dto_user import InputUser

class RepositoryUser : 
    def __init__(self, db : Database = Depends(get_db_connection)) -> None:
        self.repository = db.get_collection("user")
    
    def insert_new_user(self, new_user : InputUser) : 
        return self.repository.insert_one(new_user.dict())

