class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def get_info(self):
        return f"{self.name}, {self.age}, {self.city}"

class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
    def display_info(self):
        print(self.brand, self.model, self.year, self.color)
    def change_color(self, new_color):
        self.color = new_color

class BankAccount:
    def __init__(self, owner, account_number, balance=0.0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError()
        elif amount > 0:
            self.balance -= amount
    def check_balance(self):
        return self.balance