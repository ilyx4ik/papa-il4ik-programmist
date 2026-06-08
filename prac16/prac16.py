from abc import ABC, abstractmethod

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class BookPrinter:
    @staticmethod
    def print_book(book: Book):
        print(book.title, book.author)

class BookRepository:
    def save(self, book: Book):
        pass

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        pass

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        pass

class CryptoPayment(PaymentProcessor):
    def process_payment(self, amount):
        pass

class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailSender(MessageSender):
    def send(self, message):
        pass

class SmsSender(MessageSender):
    def send(self, message):
        pass

class PushSender(MessageSender):
    def send(self, message):
        pass

class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender
    def notify(self, message):
        self.sender.send(message)