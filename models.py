from abc import ABC, abstractmethod

# create a base class name - libraryitem
class LibraryItem(ABC):

    total_items = 0

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.__available = True  # private set default to true

        LibraryItem.total_items += 1 # update the class attributes via class instance


    # method to return private value (need to check if item is available or not)
    def is_available(self):
        return self.__available

    # when borrowed by a person, makr it unavailable
    def mark_borrowed(self):
        self.__available = False

    # when returned by a person, then it is again available
    def mark_returned(self):
        self.__available = True

    # abstract method, enforce every child class to have this method
    @abstractmethod
    def late_fee(self, days_late):
        pass


class Book(LibraryItem):
    DAILY_RATE = 2

    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)

        self.author = author

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return f"Book: {self.title} by {self.author}  (ID : {self.item_id}"


class Magazine(LibraryItem):
    DAILY_RATE = 1

    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        f"Magazine: {self.title} having issue number :  {self.issue_number}  (ID : {self.item_id}"


class DVD(LibraryItem):
    DAILY_RATE = 5

    def __init__(self, title, item_id, duration_minutes):
        super().__init__(title, item_id)
        self.duration_minutes = duration_minutes


    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        f"DVD: {self.title} has total duration of watch time : {self.duration_minutes}"

#--------------------------------------------------------------- member class ----------------------------

class Member:
    def __init__(self, name, member_id, max_item = 3):
        self.name = name
        self.member_id = member_id
        self.max_item = max_item

        self.__borrowed = [] # private list of borrow items for member


    def borrowed(self, item):
        # raise value error if not available (can borrow only if available)
        if not item.is_available():
            raise ValueError(f"{item.title} is not available and may already have borrowed")

        if len(self.__borrowed) >= self.max_item:
            raise ValueError(f"{self.name} has already reached the max limit")

        item.mark_borrowed()
        self.__borrowed.append(item)
        print(f"{self.name} borrow {item.title}")


    def return_item(self, item, days_late = 0):
        # raise error if not borrowed by the member
        if item not in self.__borrowed:
            raise ValueError(f"{item.title} not in {self.name}'s borrowed list")

        fee = item.late_fee(days_late)
        item.mark_returned()
        self.__borrowed.remove(item)
        print(f"{self.name} has returned {item.title} and has incurred fee of {fee}")
        return fee

    def borrow_titles(self):
        return [item.title for item in self.__borrowed]






