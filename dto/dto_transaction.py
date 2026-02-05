from typing import List
from pydantic.v1 import BaseModel
from typing import Optional
from datetime import date, datetime

from enums.enums_method import MetodeTransaksi
from enums.enums_tipe import TipeTransaksi
from dto.dto_common import pageBase  
from model.model_transaction import transaksi
from bson import ObjectId
from util.util_date_time import convert_datetime_str

class InputTransaksi(BaseModel): 
    tipe : TipeTransaksi
    metode : MetodeTransaksi
    nama: str
    amount: float
    keterangan: Optional[str] 
    status: bool

class OutputTransactionPage(pageBase): 
    data : List[transaksi]

class Config : 
        json_encoders ={ObjectId : str, datetime : convert_datetime_str}