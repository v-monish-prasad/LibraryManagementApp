class LibraryItem:
    def __init__(self, id, title, year):
        self.__id = id
        self.title = title
        self.year = year

    def getId(self):
        return self.__id

    def displayLibraryItemDetails(self):
        print("Library Item : ")
        print("ID : ", self._LibraryItem__id)  # in python, private members can be used by "mangling" without using get function
        print("Title : ", self.title)
        print("Year : ", self.year, "\n")


class Book(LibraryItem):
    def __init__(self, id, title, year, author):
        super().__init__(id, title, year)
        self.author = author

    def displayBookDetails(self):
        print("Book : ")
        print("ID : ", self.getId())  # also accessed using getId()
        print("Title : ", self.title)
        print("Year : ", self.year)
        print("Author : ", self.author, "\n")


class Magazine(LibraryItem):
    def __init__(self, id, title, year, issue):
        super().__init__(id, title, year)
        self.issue = issue

    def displayMagazineDetails(self):
        print("Magazine : ")
        print("ID : ", self.getId())
        print("Title : ", self.title)
        print("Year : ", self.year)
        print("Issue no. : ", self.issue)


libraryItem = LibraryItem(1, "Alchemist", 1980)
libraryItem.displayLibraryItemDetails()

book = Book(2, "Siddhartha", 2000, "Siddharth")
book.displayBookDetails()

magazine = Magazine(3, "Marvel Comics", 2020, 3)
magazine.displayMagazineDetails()

