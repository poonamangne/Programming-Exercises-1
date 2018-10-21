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
        return format(self.__balance, ".2f")
    
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
        if self.__balance - amount > 0: # Check if withdrawal is possible
            balanceAmount = self.__balance - amount
            self.setBalance(balanceAmount)
        else:
            print("Insufficient balance in account, withdraw unsuccessful!")
    
    def deposit(self, amount):
        balanceAmount = self.__balance + amount
        self.setBalance(balanceAmount)