from typing import Optional 
from bson import ObjectId
from pydantic.v1 import BaseModel, Field 

from model.model_common import PyObjectId
from enums.enums_method import MetodeTransaksi 
from enums.enums_tipe import TipeTransaksi

class transaksi(BaseModel):
    id : PyObjectId = Field(alias='_id') 
    tipe : TipeTransaksi
    metode : MetodeTransaksi
    nama: str
    amount: float
    keterangan: Optional[str] = None
    status: bool

    class Config : 
        json_encoders ={ObjectId : str}