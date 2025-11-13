# 1-misol
class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.__account_number = account_number
        self.__customer_name = customer_name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    # Balansni oshirish
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} so‘m qo‘shildi. Yangi balans: {self.__balance} so‘m.")
        else:
            print("Xatolik: kiritilgan summa musbat bo‘lishi kerak!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} so‘m yechildi. Qolgan balans: {self.__balance} so‘m.")
        else:
            print("Xatolik: balans yetarli emas yoki noto‘g‘ri summa kiritildi.")

    def account_info(self):
        print(f"Mijoz: {self.__customer_name} | Hisob raqami: {self.__account_number}")


class PremiumAccount(BankAccount):
    def __init__(self, account_number, customer_name, balance=0, discount_rate=0.02):
        super().__init__(account_number, customer_name, balance)
        self.__discount_rate = discount_rate

    def withdraw(self, amount):
        discounted_amount = amount * (1 - self.__discount_rate)
        print(f"Chegirma qo‘llanildi ({self.__discount_rate*100}%), to‘lov: {discounted_amount} so‘m.")
        super().withdraw(discounted_amount)
