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



b = LibraryBook("Гарри Поттер", "777")

b.take_book("123")
b.take_book("777")
b.return_book()
