class Book:
    def __init__(self,title,author,isbn) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    #实现借书
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False
    #实现还书
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False
    #自定义字符串输出
    def __str__(self) -> str:
        status = "Avaliable" if not self.is_borrowed else "Borrowed"
        return f"{self.title} by {self.author} (ISBN{self.isbn}) - {status}"