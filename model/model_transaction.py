from datetime import datetime
from typing import Optional 
from bson import ObjectId
from pydantic.v1 import BaseModel, Field 

from model.model_common import PyObjectId
from enums.enums_method import MetodeTransaksi 
from enums.enums_tipe import TipeTransaksi
from util.util_date_time import convert_datetime_str


class transaksi(BaseModel):
    id : PyObjectId = Field(alias='_id', default_factory=ObjectId)
    created_time : datetime = Field(default_factory=datetime.now) 
    tipe : TipeTransaksi
    metode : MetodeTransaksi
    nama: str
    amount: float
    keterangan: Optional[str] = None
    status: bool
    user_id = str

    class Config : 
        json_encoders ={ObjectId : str, datetime :convert_datetime_str}