from enum import Enum

class TipeTransaksi(str, Enum) : 
    def __str__(self):
        return str(self.value)
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"
    INVEST = "INVEST"
    DEPOSIT = "DEPOSIT"
    BONDS = "BONDS"
