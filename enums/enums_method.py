from enum import Enum

class MetodeTransaksi(str, Enum) : 
    def __str__(self):
        return str(self.value)
    CASH = "CASH"
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"
    EWALLET = "EWALLET"
    KRIPTO = "KRIPTO"