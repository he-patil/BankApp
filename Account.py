from locale import currency
from Bank import Bank

class Account():
    currentId = -1

    def __init__(self, accId, accNumber, bank, balance):
        self.accId = accId
        self.accNumber = accNumber
        self.bank = bank
        self.balance = balance
    
    @staticmethod
    def createAccount(bankAbbr, accNumber):
        isBankExist, bank = Bank.findBankAbbr(bankAbbr)
        if isBankExist:
            Account.currentId+=1
            return True, Account(Account.currentId, accNumber, bank, 1000)
        return False, "Bank does not exist"

    def isSufficientBalance(self, amount):
        if self.balance >= amount:
            return True
        return False

    def showAccount(self):
        print(self.accId," ", self.accNumber," ", self.bank.bankId," ",self.bank.fullName," ",self.bank.bankAbbr," ",self.balance)
        
    
        