class Bank:
    def __init__(self,accno,name,acctype,balance=0):
        self.accno=accno
        self.na=name
        self.acctype=acctype
        self.bal=balance
    def deposit(self,amount):
        if amount>0:
            self.bal+=amount
            print(f"Deposit successfull,new balance:{self.bal}")
        else:
            print(f"invalid deposit amount.please enter a positive value")
    def withdraw(self,amount):
         if amount>0:
             if amount<=self.bal:
                 self.bal-=amount
                 print(f"withdrawal successfull,new balance:{self.bal}")
             else:
                 print(f"insufficient balance")
         else:
             print(f"invalid withdrawal.please enter a positive value")
    def display(self):
         print(f"account number:{self.accno}\n account holder name:{self.na}")
         print(f"\n account type:{self.acctype}\n balance:{self.bal}")
         print(f"***menu***")
         print(f"1.deposit \n 2.withdraw \n 3.diplay \n 4.exit")
b1=Bank(1002,"nidhi","savings",0)
b1.display()
while True:
    choice=int(input("enter  your choice(1-4):"))
    if choice==1:
        d=int(input("enter amount to be deposited:"))
        b1.deposit(d)
    elif choice==2:
        w=int(input("enter amount to withdraw:"))
        b1.withdraw(w)
    elif choice==3:
        b1.display()
    elif choice==4:
        print("exiting...... thank you!")
        break
    else:
        print("enter valid choice")
