# Readme file

## 1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?
## --> LibraryItem abstract means it is the blueprint item for library, and it will be instantiated via object. It lacks late fee structure method.

## --> late fee is abstract method of library items and it enforce the child class to have this, if not implemented it will through error (TypeError)


## 2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?

## --> If we read item.__available outside the class it will raise error because this is private class and put encapsulation and can not be accessed outside class

## --> is_available() method safely return the available status and does not voilates the encapsulation rules


## 3. What is the difference between LibraryItem.total_items and self.title?

## --> LibraryItem.total_items is class attributes and find the cumulative sum of items available in the library, but self.title is an instance attribute (the word self stand for that instance and not for class) and responible for that object only.

