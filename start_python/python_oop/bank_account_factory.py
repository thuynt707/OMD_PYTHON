import json
import os
import sys

current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
csv_file = os.path.join(current_dir, "bank_accounts.csv")
json_file = os.path.join(current_dir, "bank_accounts.json")

class BankAccount:
    #Magic methods
    def __init__(self, account_number, account_name, balance=0):
        self._account_number = account_number
        self._account_name = account_name
        self.set_balance(balance)
    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            print("Balance cần >=0.")
    def get_account_number(self):
        return self._account_number
    def get_account_name(self):
        return self._account_name
    def get_balance(self):
        return self._balance
    def display(self):
        print(f"Thong tin tai khoan: {self.get_account_number()} {self.get_account_name()} {self.get_balance()}")
    def withdraw(self, amount):
        if 0 < amount < self.get_balance():
            self.set_balance(self.get_balance()- amount)
        else:
            print ("Số tiền cần rút không hợp lệ")
    def deposit(self, amount):
        if amount > 0 :
            self.set_balance(self.get_balance()+ amount)
        else:
            print ("Số tiền cần nạp không hợp lệ")
    @classmethod
    def from_json(cls, json_file):
        accounts = []
        with open(json_file) as file:
            reader = json.load(file)
            for object in reader:
                accounts.append(cls(**object))
        return accounts 
    def __repr__(self):
        return f"Thong tin tai khoan: {self.get_account_number()} {self.get_account_name()} {self.get_balance()}"

json_accounts = BankAccount.from_json(json_file)
for account in json_accounts:
    print(account)