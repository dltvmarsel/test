from abc import ABC, abstractmethod

# --- Абстракция ---
class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class CardPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата {amount}₽ через банковскую карту")

    def refund(self, amount):
        print(f"Возврат {amount}₽ на банковскую карту")


class CryptoPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата {amount}$ в криптовалюте")

    def refund(self, amount):
        print(f"Возврат {amount}$ в криптовалюту")


# --- Инкапсуляция ---
class LibraryBook:
    def __init__(self, title, code):
        self.title = title
        self._is_taken = False
        self.__secret_code = code

    def take_book(self, code):
        if code == self.__secret_code and not self._is_taken:
            self._is_taken = True
            print(f'Взяли "{self.title}"')
        else:
            print("Не получилось")

    def return_book(self):
        self._is_taken = False
        print(f'Вернули "{self.title}"')


# --- Демонстрация ---
if __name__ == "__main__":
    # Работа с книгой (инкапсуляция)
    book = LibraryBook("Гарри Поттер", "777")
    book.take_book("777")
    book.return_book()

    print()

    # Работа с оплатой (абстракция)
    card = CardPayment()
    crypto = CryptoPayment()

    card.pay(500)
    card.refund(200)

    crypto.pay(0.05)
    crypto.refund(0.02)
