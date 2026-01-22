from fastapi import Depends 
from pydantic.v1 import parse_obj_as 
from typing import List 
from pymongo.database import Database 
from config.config import get_db_connection 
from dto.dto_user import InputUser

class RepositoryUser : 
    def __init__(self, db : Database = Depends(get_db_connection)) -> None:
        self.repository = db.get_collection("user")
    
    def register_user(self, new_user : InputUser) : 
        return self.repository.insert_one(new_user.dict())

    def get_list_user(self, match_filter : dict)  : 
        results = self.repository.find(match_filter)
        results = list(results)
        return parse_obj_as(List[InputUser], results)
        