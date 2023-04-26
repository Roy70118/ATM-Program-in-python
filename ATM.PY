
import sys


class Atm:

    def __init__(self):
        self.pin = 1234
        self.balance = 20000
        self.menu()

    def menu(self):
        print("""
            what would you like to do!
                1. check balance
                2.withdraw balance
                3.Deposit balance
                4.Exit
                """)
        option = int(input("Enter your option: "))
        if option == 1:
            self.check_balance()

        elif option == 2:
            self.withdrawal()

        elif option == 3:
            self.Deposit()

        elif option == 4:
            sys.exit()

    def check_balance(self):
        input_pin = int(input("Enter your pin: "))
        if input_pin == self.pin:
            print("*" * 50)
            print(f"Your balance is {self.balance}")
            print("*"*50)
        else:
            print("Your pin is incorrect")
        self.menu()

    def withdrawal(self):
        input_pin = int(input("Enter your pin: "))
        if input_pin == self.pin:
            input_balance = int(input("Enter your withdrawal amount: "))
            if input_balance <= self.balance:
                self.balance = self.balance - input_balance
                print("*" * 50)
                print(f"your updated balance is {self.balance}")
                print("*" * 50)
            else:
                print(" you dont have that much balance")
        else:
            print(" your pin is incorrect!")
        self.menu()

    def Deposit(self):
        input_pin = int(input("Enter your pin: "))
        if input_pin == self.pin:
            input_deposit = int(input("Enter your deposit amount: "))
            self.balance = self.balance + input_deposit
            print("*" * 50)
            print(f" your updated balance is {self.balance}")
            print("*" * 50)
        else:
            print(" your pin is incorrect")
        self.menu()


sbi = Atm()
