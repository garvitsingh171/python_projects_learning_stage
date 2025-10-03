class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,adding):
        self.balance = self.balance + adding
        return self.balance
    
    def withdraw(self,taking):
        self.balance = self.balance - taking
        return self.balance
    
own = "Shreshtha Yadav"
bal = 200000000000
add = 300000000
tak = 4000000

shre_account = Account(own,bal)

print(f'{own} have bank balance {bal}')
print(shre_account.deposit(add))
print(shre_account.withdraw(tak))