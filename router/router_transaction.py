from typing import Optional
from fastapi import APIRouter , Depends
from dto.dto_transaction import InputTransaksi
from enums.enums_tipe import TipeTransaksi
from service.service_transaction import ServiceTransaction 
router_transaction = APIRouter(prefix="/api/v1")

@router_transaction.post('/transaction')
def insert_new_transaction(input_transaction:InputTransaksi , service_transaction : ServiceTransaction = Depends()) : 
    service_transaction.insert_new_transaction(input_transaction)
    return input_transaction

@router_transaction.get('/transaction')
def get_list_transaction(tipe: Optional[TipeTransaksi] = None, service_transaction : ServiceTransaction = Depends()) :
     return service_transaction.get_list_transaction(tipe)
