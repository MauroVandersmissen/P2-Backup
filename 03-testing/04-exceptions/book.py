class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        if title and title != "":
            self.__title = title
        else:
            raise RuntimeError("Title cannot be empty.")

    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, isbn):
        if self.isbn_valid(isbn):
            self.__isbn = isbn
        else:
            raise RuntimeError("Invalid ISBN.")
        
    @staticmethod
    def isbn_valid(isbn):
        digits = [int(d) for d in isbn.replace("-", "").replace(" ", "")]
        if len(digits) != 13:
            return False
        total = 0
        for i in range(13):
            if i % 2 == 0:
                total += digits[i]
            else:
                total += digits[i] * 3
        return total % 10 == 0
    
    def __repr__(self):
        return f"Name: {self.title}, ISBN: {self.isbn}"
    

book = Book("Watchmen", "978-1779501127") 
print(book)
# book = Book("", "978-1779501127")
# print(book) 
# book = Book("Watchmen", "978-17795011278")
# print(book)