class Member:
    def __init__(self,name,member_id) -> None:
        self.name = name
        self.member_id = member_id
        self.brrowed_books = []
        
    #借书
    def brrow_books(self, book):
        if book.borrow():
            self.brrowed_books.append(book)
            return True
        return False
    
    #还书
    def return_book(self, book):
        if book.return_book():
            self.brrowed_books.remove(book)
            return True
        return False
    
    #自定义格式化输出
    def __str__(self) -> str:
        return f"Member:{self.name},(ID:{self.member_id})"