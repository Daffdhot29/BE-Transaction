from typing import Annotated, Optional
from fastapi import APIRouter , Depends
from dto.dto_common import tokenData
from dto.dto_transaction import InputTransaksi
from enums.enums_tipe import TipeTransaksi
from service.service_transaction import ServiceTransaction 
from service.service_common import get_current_user


router_transaction = APIRouter(prefix="/api/v1",tags=["Transaction"])

@router_transaction.post('/transaction')
def insert_new_transaction(
    input_transaction:InputTransaksi,
    current_user: Annotated[tokenData, Depends(get_current_user)] , 
    service_transaction : ServiceTransaction = Depends()) : 
    service_transaction.insert_new_transaction(input_transaction, current_user)
    return input_transaction

@router_transaction.get('/transaction')
def get_list_transaction(
    current_user : Annotated[tokenData, Depends(get_current_user)],
    tipe: Optional[TipeTransaksi] = None, 
    # pagination buat membagi data besar jadi beberapa halaman
    page : int = 0,
    size: int = 10,
    service_transaction : ServiceTransaction = Depends()
    ) :
    return service_transaction.get_list_transaction( tipe, page,size,current_user)

@router_transaction.post('/export')
def export_file(
    current_user : Annotated[tokenData, Depends(get_current_user)], 
    start_time : Optional[str]=None, 
    end_time: Optional[str] = None, 
    tipe: Optional[TipeTransaksi] = None, 
    service_transaction : ServiceTransaction = Depends()
    ) :
    