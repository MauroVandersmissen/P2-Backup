class Book:
    def __init__(self,title,isbn):
        self.title=title
        self.isbn=isbn

        @property
        def title(self):
            return self.__title
        
        @title.setter
        def title(self,title):
            if title and title!="":
                self.__title=title
            else:
                raise RuntimeError

        @property
        def isbn(self):
            return self.__isbn
        
        @isbn.setter
        def isbn(self,isbn):
            if isbn_valid(isbn):
                self.__isbn=isbn
            else:
                raise RuntimeError
            
        def isbn_valid(isbn):
            digits=[isbn.strip("- ")]
            if len(digits)!=13:
                return False
            for i in range(len(digits)):
                if i%2!=0:
                    [i]=digits[i]*3
            if sum(digits)%10!=0:
                return False
            return True