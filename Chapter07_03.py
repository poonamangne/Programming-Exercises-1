# 7.3 Write a test program that creates an Account object


class Account:

    # Construct a Account object with default values
    def __init__(self, id = 0, balance = 100, annualInterestRate = 0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 1200

    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()

    def withdraw(self, amount):
        if self.__balance - amount > 0:  # Check if withdrawal is possible
            balanceAmount = self.__balance - amount
            self.setBalance(balanceAmount)
        else:
            print("Insufficient balance in account, withdraw unsuccessful!")

    def deposit(self, amount):
        balanceAmount = self.__balance + amount
        self.setBalance(balanceAmount)


def main():
    # Create a Account object
    account1 = Account(1122, 20000, 4.5)

    account1.withdraw(2500)  # Withdraw

    account1.deposit(3000)  # Deposit

    # Display id, balance, monthly interest rate, and monthly interest of the account object
    print("Account Details")
    print("ID:", account1.getId())
    print("Balance: $" + str(account1.getBalance()))
    print("Monthly Interest Rate: " + format(account1.getMonthlyInterestRate(), ".2%"))
    print("Monthly Interest: $" + format(account1.getMonthlyInterest(), ".2f"))


main()  # Call the main function
