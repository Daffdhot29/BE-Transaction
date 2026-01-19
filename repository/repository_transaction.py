
from fastapi import Depends
from pydantic.v1 import parse_obj_as
from typing import List
from pymongo.database import Database
from config.config import get_db_connection
from model.model_transaction import transaksi
from dto.dto_transaction import InputTransaksi

class RepositoryTransaction: 
    def __init__(self , db : Database = Depends(get_db_connection)) -> None: 
        self.repository = db.get_collection("transaction")

    def insert_new_transaction(self, new_transaction: InputTransaksi):
        return self.repository.insert_one(new_transaction.dict())

    def get_list_transaction(self, match_filter : dict):
        results =  self.repository.find(match_filter) 
        results = list(results)
        return parse_obj_as(List[transaksi], results)