class Library:
    def __init__(self) -> None:
        self.books = []
        self.members = []
        
    #添加书籍
    def add_books(self,book):
        self.books.append(book)
    
    #添加成员
    def add_member(self,member):
        self.members.append(member)
        
    #通过ISBN找到一本书
    def find_book_by_isbn(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    #通过用户id找到用户
    def find_member_by_id(self,member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    
    #自定义格式化输出
    def __str__(self) -> str:
        book_list = "\n".join(str(book) for book in self.books)    
        member_list = "\n".join(str(member) for member in self.members)
        return f"Library Books:\n{book_list}\n\nLibrary Members:\n{member_list}"