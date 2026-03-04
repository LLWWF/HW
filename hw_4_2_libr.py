class LibraryBook:
    __last_id = 1
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__book_id = LibraryBook.__generate_id()
        self._status = "доступна"
    
    @staticmethod
    def __generate_id():
        LibraryBook.__last_id += 1
        return LibraryBook.__last_id
    
    @property
    def status(self):
        return self._status
    
    @property
    def book_id(self):
        return self.__book_id
    
    def borrow(self):
        if self._status == "доступна":
            self._status = "выдана"
            print(f"Книга '{self.title}' выдана")
        else:
            print(f"Книга '{self.title}' уже выдана")
    
    def return_book(self):
        if self._status == "выдана":
            self._status = "доступна"
            print(f"Книга '{self.title}' возвращена")
        else:
            print(f"Книга '{self.title}' уже доступна")
    
    def get_info(self):
        return {
            "ID": self.__book_id,
            "Название": self.title,
            "Автор": self.author,
            "Статус": self._status
        }
    
    @classmethod
    def from_string(cls, book_string):
        parts = book_string.split(" - ")
        if len(parts) != 2:
            print("Неверный формат строки. Используйте 'Автор - Название'")
            
        author, title = parts
        author = author.strip()
        title = title.strip()
        return cls(title, author)
    
    def __str__(self):
        return f"'{self.title}' - {self.author} (ID: {self.__book_id}, Статус: {self._status})"


