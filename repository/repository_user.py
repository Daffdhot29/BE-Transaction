from fastapi import Depends 
from pymongo.database import Database 
from config.config import get_db_connection 
from dto.dto_user import InputUser,InputLogin
from model.model_user import UserTransaction

class RepositoryUser : 
    def __init__(self, db : Database = Depends(get_db_connection)) -> None:
        self.repository = db.get_collection("user")
    
    def insert_new_user(self, new_user : InputUser) : 
        return self.repository.insert_one(new_user.dict())

    def find_userBy_username(self, username : str) : 
        filter = self.repository.find_one({
            "username" : username
        })
        if filter is not None : 
            return UserTransaction.parse_obj(filter)
        return None

    def findUser_by_usernameNPassword(self, Login : InputLogin) : 
        filter = self.repository.find_one({ 
            "username" : Login.username,
            "password" : Login.password
        })
        
        if filter is not None : 
            return UserTransaction.parse_obj(filter)
        return None
