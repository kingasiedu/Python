# bank account class

class BankAccount:
    def __init__(self, pin, balance, amount):
        self.pin = 214
        self.balance = 0
        self.amount = 0

    # function to deposit amount
    def deposit(self):
        amount = float(input("Enter amount to be deposited:"))
        self.pin = int(input("Enter your pin"))
        while self.pin == 214:
            print("This is your amount", amount)
        else:
            print("Wrong pin Enter a new pin")

        self.balance += amount
        return deposited
        print("\n Amount deposited:", amount)

    # function to withdraw the amount
    def withdraw(self):
        amount = float(input("Enter the amount you want to withdraw:"))
        self.pin = int(input("Enter your pin"))
        if self.pin == 214:
            pass
        else:
            print("Enter a new pin")

        if self.balance >= amount:
            self.balance -= amount
            print("\n You withdrew:", amount)
        else:
            print("\n Your balance is not enough")

    def get_balance(self,):

        print("\n Your available balance is:", self.balance)


s1 = BankAccount(214, 0, 0)

s1.deposit()
s1.withdraw()
s1.get_balance()
