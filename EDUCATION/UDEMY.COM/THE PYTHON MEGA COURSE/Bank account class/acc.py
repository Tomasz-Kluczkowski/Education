class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, "r") as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, "w") as file:
            file.write(str(self.balance))


class Checking(Account):
    """This class generates checking account"""

    acc_type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


account = Account("balance.txt")
print(account)
account.withdraw(100)
account.commit()
print(account.balance)
account.deposit(150)
account.commit()
print(account.balance)

checking = Checking("balance.txt", 5)
checking.transfer(100)
checking.commit()
print("checking:", checking.balance)