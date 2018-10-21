# 12.3 ATM machine Game

from Account import Account

def main():
    accountList = []
    
    for i in range(0, 10):
        acct = Account(i, 100, 0)
        accountList.append(acct)
    
    while True:
        accountID = eval(input("Enter an account id: "))
        if 0 <= accountID <= 9:
            for obj in accountList:
                if accountID == obj.getId(): 
                    break
            while True:
                print()
                print("Main menu")
                print("1: check balance")
                print("2: withdraw")
                print("3: deposit")
                print("4: exit")
                choice = eval(input("Enter a choice: "))             
                if choice == 1:
                    print("The balance is", obj.getBalance())
                elif choice == 2:
                    amount = eval(input("Enter an amount to withdraw: "))
                    obj.withdraw(amount) 
                elif choice == 3:
                    amount = eval(input("Enter an amount to deposit: "))
                    obj.deposit(amount)
                else:
                    print()
                    break                                  
        else:
            print("Incorrect account id, try again!")
    
    
            
main()