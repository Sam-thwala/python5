class Book:
    def __init__(self):
        self.__bookpages = 100  # Private attribute

    def read_book(self):
        if self.__bookpages > 0:
            self.__bookpages = 1
            print("One page read!")
        else:
            print("No pages read")

Read= Book()
Read.read_book()