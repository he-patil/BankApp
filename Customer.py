from Account import Account

class Customer():
    currentId = -1
    allCustomers = []

    def __init__(self, customerId, userName, firstName, lastName):
        self.userName = userName
        self.firstName = firstName
        self.lastName = lastName
        self.totalBalance = 0
        self.accounts = []
    
    @staticmethod
    def createCustomer(userName, firstName, lastName):
        Customer.currentId+=1
        customer = Customer(Customer.currentId, userName, firstName, lastName)
        Customer.allCustomers.append(customer)
        return customer
    
    @staticmethod
    def findCustomer(userName):
        for customer in Customer.allCustomers:
            if customer.userName == userName:
                return True, customer
        return False, None            

    def findAccount(self, bankAbbr):
        for account in self.accounts:
            if account.bank.bankAbbr == bankAbbr:
                return True, account
        return False, None

    def __updateTotalBalance(self):
        self.totalBalance = 0
        for account in self.accounts:
            self.totalBalance+=account.balance

    def addAccount(self, accNumber, bankAbbr):

        isAccountExist, account = self.findAccount(bankAbbr)
        if isAccountExist:
            return False, "Account already exist with same bank"

        isAccountCreated, account = Account.createAccount(bankAbbr, accNumber)
        if not isAccountCreated:
            return False, account

        self.accounts.append(account)
        self.__updateTotalBalance()
        return True, account

    def deposit(self, bankAbbr, amount):
        isAccountExist, account = self.findAccount(bankAbbr)
        if not isAccountExist:
            return False, "Account not found"
        
        account.balance+=amount
        self.__updateTotalBalance()
        return True, amount
    
    def withdraw(self, bankAbbr, amount):
        isAccountExist, account = self.findAccount(bankAbbr)
        if not isAccountExist:
            return False, "Account not found"
        if not account.isSufficientBalance(amount):
            return False, "Insufficient balance"
        
        account.balance-=amount
        self.__updateTotalBalance()
        return True, amount

    def transfer(self, userName, creditBankAbbr, debitBankAbbr, amount):
        isCustomerExist, customer = Customer.findCustomer(userName)
        if not isCustomerExist:
            return False, "Customer does not exist"
        
        isWithdrawn, amount = self.withdraw(debitBankAbbr, amount)
        if isWithdrawn:
            isDeposited, amountD = customer.deposit(creditBankAbbr, amount)
            if not isDeposited:
                self.deposit(debitBankAbbr, amount)
                return False, amountD
            return True, "Transfer Success"
        return False, amount

        
    def transferSelf(self, creditBankAbbr, debitBankAbbr, amount):
        return self.transfer(self.userName, creditBankAbbr, debitBankAbbr, amount)

    @staticmethod
    def showCustomer():
        for cust in Customer.allCustomers:
            print(cust.userName," ",cust.firstName," ",cust.lastName," ", cust.totalBalance)
            for acc in cust.accounts:
                acc.showAccount()
            print()

        