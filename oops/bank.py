# instance variable => binded by object accessed using object(self)
# static variable => binded by class accessed using class name 

class bank:
    acno:int
    ac_type:str
    balance:int
    bank_name:str="SBI" #static variable
    holder_name:str
    ifsc_code:str

    def __init__(self,acno,ac_type,balance,bank_name,holder_name,ifsc_code):
        self.acno=acno
        self.ac_type=ac_type
        self.balance=balance
        self.holder_name=holder_name
        self.ifsc_code=ifsc_code
    
    def withdraw(self,amount):
        if self.balance>amount:
            self.balance-=amount
            print(f"your {bank.bank_name} account has debited with amount {amount} avialable balance {self.balance}")
        else:
            print("transaction declined....")
    
    def deposit(self,amount):
        self.balance+=amount
        print(f"your {bank.bank_name} account has debited with amount {amount} avialable balance {self.balance}")
    
    def balance_enq(self):
        print(f"your {bank.bank_name} account balance is {self.balance}")
    

obj=bank(1234,"savings",3245,"dhanuja","ADF1245")
obj.balance_enq()
obj.withdraw(200)
obj.deposit(500)
