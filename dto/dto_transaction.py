from typing import List
from pydantic.v1 import BaseModel
from typing import Optional

from enums.enums_method import MetodeTransaksi
from enums.enums_tipe import TipeTransaksi
from dto.dto_common import pageBase  
from model.model_transaction import transaksi
from bson import ObjectId

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
        json_encoders ={ObjectId : str}