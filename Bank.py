class Bank():
    bankIdCurrent = -1
    allBanks = []
    def __init__(self, bankId, fullName, bankAbbr):
        self.bankId = bankId
        self.fullName = fullName
        self.bankAbbr = bankAbbr

    @staticmethod
    def findBankAbbr(bankAbbr):
        for bank in Bank.allBanks:
            if bank.bankAbbr == bankAbbr:
                return True, bank
        return False, None

    @staticmethod
    def findBankName(fullName):
        for bank in Bank.allBanks:
            if bank.fullName == fullName:
                return True, bank
        return False, None

    @staticmethod
    def createBank(fullName, bankAbbr):
        isBankExist, bank = Bank.findBankAbbr(bankAbbr)
        if isBankExist:
            return False, bank, "Bank Abbreviation already exist"

        isBankExist, bank = Bank.findBankName(fullName)
        if isBankExist:
            return False, bank, "Bank Name already exist"
        
        Bank.bankIdCurrent+=1
        bank = Bank(Bank.bankIdCurrent, fullName, bankAbbr)
        Bank.allBanks.append(bank)
        return True, bank, "Bank Created"
    
    @staticmethod
    def showBanks():
        for bank in Bank.allBanks:
            print(str(bank.bankId)+": "+bank.fullName+"- "+bank.bankAbbr)
        print()
    

    

