

from pydantic.v1 import BaseModel
from typing import Optional
from enums.enums_method import MetodeTransaksi
from enums.enums_tipe import TipeTransaksi

class InputTransaksi(BaseModel): 
    tipe : TipeTransaksi
    metode : MetodeTransaksi
    nama: str
    amount: float
    keterangan: Optional[str] = None
    status: bool
