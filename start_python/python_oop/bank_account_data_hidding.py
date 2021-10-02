class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self._account_number = account_number
        self._account_name = account_name

        # Gọi set_balance để validate
        # thay vì self._balance = balance
        self.set_balance(balance)

    def get_account_number(self):
        return self._account_number

    def get_account_name(self):
        return self._account_name

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            # raise phát ra một ngoại lệ (lỗi)
            # Tạm thời chấp nhận sử dụng print
            raise ValueError("Số dư phải lớn hơn 0")

    def display(self):
        # Khi sử dụng getter và setter, các phương thức khác cần truy cập
        # thuộc tính cũng nên gọi qua getter và setter
        print(self.get_account_number(),
              self.get_account_name(), self.get_balance(), "₫")

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
        else:
            raise ValueError(
                "Số tiền phải lớn hơn 0 và không được vượt quá số dư hiện tại")

    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance() + amount)
        else:
            raise ValueError("Số tiền phải lớn hơn 0")


my_account = BankAccount(1, "Ba", 1_000_000_000_000_000_000)
my_account.deposit(1_000_000_000_000_000_000)
my_account.display()

my_account.withdraw(100_000_000)  # quá nhỏ bé 😊
my_account.display()
