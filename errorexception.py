class LowBalance(Exception):
    def __init__(self, a , b):
        self.acc = a
        self.bal = b

    def getDetail(self):
        return self.acc,self.bal

class Account:
    def __init__(self, a, b):
        self.ac = a
        self.bal = b

    def withdraw(self):
        a = int(input("Enter money to be withdrawn >>>  "))
        if self.bal > a:
            print("Money Withdrawn")
            self.bal -= a
            print(f"Available Balance {self.bal}")
        else:
            raise LowBalance(self.ac,self.bal)

a1 = Account("1243XXXXXX78",10000)
try:
    a1.withdraw()
except LowBalance as e:
    acc , bal = e.getDetail()
    print(f"Insufficient balance in {acc} , Current Balance is {bal}")
