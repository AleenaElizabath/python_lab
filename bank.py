class Account:
    def __init__(self,name,acc_no,acc_type,bal):
        self.bal=0
        self.name=name
        self.acc_no=acc_no
        self.acc_type=acc_type
        
    def display(self):
        print("Name of the aacount holder=",self.name)
        print("Account number=",self.acc_no)
        print("Account type=",self.acc_type)
        print("Current balance=",self.bal)

    def deposit(self):
        amount=float(input("Enter the amount to deposit:"))
        self.bal+=amount
        print("You deposited Rs.",amount)

    def withdraw(self):
        amount=float(input("Enter the amount to Withdraw:"))
        if self.bal<amount:
            print("You do not have sufficient balance")
        else:
            self.bal-=amount
            print("You Withdrew Rs.",amount)
name=input("Enter the name of the account holder:")
acc_type=input("Enter the type of account:(Savings/FD)")
acc_no=int(input("Enter the account number:"))
print('''Bank Account Application:
1.Enter details
2.Withdraw
3.Deposit
4.Display Details
5.Exit''')
ch=" "
s=Account(name,acc_no,acc_type,0)
while(ch!=5):
    ch=int(input("Enter the choice:(1/2/3/4/5):"))
    if ch==1:
        s.details()
    elif ch==2:
        s.withdraw()
    elif ch==3:
        s.deposit()
    elif ch==4:
        s.display()
    elif ch==5:
        exit(0)
    else:
        print("Invalid input")
        
