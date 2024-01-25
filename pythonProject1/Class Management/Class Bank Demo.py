class Bank:
    def openAccount(self,cname,acno,balance):
        self.cname=cname
        self.acno=acno
        self.balance=balance
        print("Hello",self.cname,"Your Account No",self.acno,"is Opened With",self.balance,"Rs.")

    def deposit(self,amount):
        self.balance=self.balance + amount
        self.checkbalance()
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            self.checkbalance()
        else:
            print("Insufficent Balance")
    def checkbalance(self):
        print("Current Balance Is ",self.balance,"Rs.")
b1=Bank()
cname=input("Enter Your Name : ")
acno=int(input("Enter Your Account Number : "))
balance=int(input("Enter Initial Balance : "))
b1.openAccount(cname,acno,balance)
while True:
    print("*"*50)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice=int(input("Enter Your Choice : "))
    print("*"*50)

    if choice==1:
        amount=int(input("Enter Deposit Amount :"))
        b1.deposit(amount)
        print("*"*50)
    elif choice==2:
        amount=int(input("Enter Withdraw Amount : "))
        b1.withdraw(amount)
        print("*"*50)
    elif choice==3:
        b1.checkbalance()
        print("*"*50)
    elif choice==4:
        print("Thank you For Using Our Services.")
        print("*"*50)
        break
    else:
        print("Invelid Choise Number Please Try Again")
        print("*"*50)
