from Bank import Bank
from Customer import Customer
from Account import Account

def main():
    bank1 = Bank.createBank("State Bank", "SBI")
    bank2 = Bank.createBank("HDFC Bank", "HDFC")
    bank3 = Bank.createBank("Bank of India", "BOI")

    print("All Banks: ")
    Bank.showBanks()

    cust1 = Customer.createCustomer("user1", "UserA", "UserAA")
    cust2 = Customer.createCustomer("user2", "UserB", "UserBB")
    cust3 = Customer.createCustomer("user3", "UserC", "UserCC")

    cust1.addAccount(111,"SBI")
    cust1.addAccount(222,"BOI")
    
    cust2.addAccount(123,"HDFC")
    cust2.addAccount(321,"SBI")

    cust3.addAccount(789,"BOI")

    print("All Customers: ")
    Customer.showCustomer()
    
    print("Withdraw 500 from SBI of user1: ")
    success , message = cust1.withdraw("SBI",500)
    if not success:
        print(message)
    Customer.showCustomer()

    print("Deposit 500 in SBIN of user1: ")
    success , message = cust1.deposit("SBIN",500)
    if not success:
        print(message)
    Customer.showCustomer()

    print("Withdraw 600 from SBI of user1: ")
    success , message = cust1.withdraw("SBI",600)
    if not success:
        print(message)
    Customer.showCustomer()

    print("Transfer 500 from SBI of user1 to SBI of user2: ")
    success , message = cust1.transfer("user2","SBI","SBI",500)
    if not success:
        print(message)
    Customer.showCustomer()

    print("Self transfer 500 from user1's SBI to BOI: ")
    success , message = cust1.transferSelf("SBI","BOI",500)
    if not success:
        print(message)
    Customer.showCustomer()

if __name__ == "__main__":
    main()