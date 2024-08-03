from book import Book
from library import Library
from member import Member

def main():
    #创建图书馆对象
    library = Library()
    
    #添加书籍
    book1 = Book("1984","George Orwell","123456789")
    book2 = Book("To Kill a Mockingbird","Harper Lee","987654321")
    library.add_books(book1)
    library.add_books(book2)
    
    #添加成员
    member1 = Member("Alice","001")
    member2 = Member("Bob","002")
    library.add_member(member1)
    library.add_member(member2)
    
    #打印图书馆信息
    print(library)
    
    #借书
    print("\nAlice brrows '1984':\n")
    member1.brrow_books(book1)
    print(library)
    
    #还书
    print("\nAlice returns '1984':\n")
    member1.return_book(book1)
    print(library)
    
if __name__ == "__main__":
    main()