class Transaction:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def process(self):
        print("Processing transaction...")


class Deposit(Transaction):

    
    def deposit(self, amount, bonus=0):
        self.balance += amount + bonus
        print(f"{self.account_holder} deposited {amount}")
        if bonus > 0:
            print(f"Bonus added: {bonus}")
        print(f"New Balance: {self.balance}")

    
    def process(self):
        print("Deposit transaction processed.")


class Withdrawal(Transaction):

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_holder} withdrew {amount}")
            print(f"New Balance: {self.balance}")
        else:
            print("Insufficient funds!")

    
    def process(self):
        print("Withdrawal transaction processed.")


class Transfer(Transaction):

    def transfer(self, amount, receiver):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_holder} transferred {amount} to {receiver}")
            print(f"Remaining Balance: {self.balance}")
        else:
            print("Insufficient funds!")

    def process(self):
        print("Transfer transaction processed.")




print("DEPOSIT")
d = Deposit("Employer", 1000)
d.process()
d.deposit(500)       
d.deposit(200, 50)      

print("\n WITHDRAWAL ")
w = Withdrawal("Employer", d.balance)
w.process()
w.withdraw(300)

print("\n TRANSFER ")
t = Transfer("Employer", w.balance)
t.process()
t.transfer(400, "Employee")