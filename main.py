from models import Book, Member, Magazine, DVD

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tom & Jerry", 2, 123)
dvd = DVD("Dilwale", 3, 120)

alice = Member("Alice", 101)
bob = Member("Bob", 102, 1)

try:
    alice.borrowed(book)
    print(f"Alice has borrowed {book.describe()}")
    bob.borrowed(book)
except ValueError as e:
    print("Could not borrow", e)


try:
    bob.borrowed(magazine)
except ValueError as e:
    print("Could not borrow ", e)

try:
    alice.return_item(dvd)
except ValueError as e:
    print("Could not return ", e)


# polymorphism
items = [book, magazine, dvd]

for item in items:
    print(item.describe(),  "--> late fee for 3 days : RS", item.late_fee(3))


# 4. Class attribute shared by all objects
print("Total items created:", Book.total_items)