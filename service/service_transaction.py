import math
from dto.dto_common import tokenData
from  repository.repository_transaction import RepositoryTransaction
from dto.dto_transaction import InputTransaksi, OutputTransactionPage

from model.model_transaction import transaksi
from enums.enums_tipe import TipeTransaksi
from fastapi import Depends


class ServiceTransaction: 
    def __init__(self, repository_transaction : RepositoryTransaction = Depends()) -> None:
        self.repository_transaction = repository_transaction
    
    def insert_new_transaction(self, Input_transaction :InputTransaksi, current_user: tokenData): 
        return self.repository_transaction.insert_new_transaction(Input_transaction)
    
    
    def get_list_transaction(self, tipe : TipeTransaksi, page: int, size: int,current_tipe_user:tokenData ) :
        match_filter = {"user_id" : current_tipe_user.userId}
        if tipe : 
            match_filter["tipe"] = tipe 

        skip = page * size
        list_transaction =  self.repository_transaction.get_list_transaction(match_filter, skip, size)
        total_data = self.repository_transaction.count_list_document(match_filter)
        total_page = math.ceil(total_data/size)

        return OutputTransactionPage(page=page, size=size, totalPage=total_page, data=list_transaction)