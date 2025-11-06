# Base class for Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

# LibraryMember class
class LibraryMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    # Method to borrow a book
    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed '{book.title}'.")

    # Method to return a book
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")

    # Display member information
    def display_info(self):
        print(f"\nMember ID: {self.member_id}")
        print(f"Name: {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print(f" - {book}")
        else:
            print("No borrowed books.")

# Main program
def main():
    print("=== Library System ===")
    
    # Input member details
    member_id = input("Enter member ID: ")
    member_name = input("Enter member name: ")
    member = LibraryMember(member_id, member_name)
    
    while True:
        print("\nOptions:")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Display member info")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            book_title = input("Enter book title: ")
            book_author = input("Enter book author: ")
            book = Book(book_title, book_author)
            member.borrow_book(book)
        elif choice == "2":
            if not member.borrowed_books:
                print("No books to return.")
                continue
            print("Borrowed books:")
            for i, b in enumerate(member.borrowed_books, start=1):
                print(f"{i}. {b}")
            try:
                book_choice = int(input("Enter the number of the book to return: "))
                if 1 <= book_choice <= len(member.borrowed_books):
                    member.return_book(member.borrowed_books[book_choice-1])
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input. Enter a number.")
        elif choice == "3":
            member.display_info()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1-4.")

# Run the program
if __name__ == "__main__":
    main()
