class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, num):
        self.balance = self.balance + num

    def withdraw(self, num):
        if self.balance - num < 0:
            print('Операция не возможна')
        else:
            self.balance = self.balance - num

    def show_balance(self):
        print(self.balance)


a = Account('aa', 200)
a.deposit(200)
a.show_balance()
a.withdraw(500)
a.withdraw(300)
a.show_balance()