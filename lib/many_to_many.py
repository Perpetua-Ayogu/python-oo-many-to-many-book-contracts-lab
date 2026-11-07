class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author is self]

    def books(self):
        books = []
        for contract in self.contracts():
            if contract.book not in books:
                books.append(contract.book)
        return books

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def sign_contracts(self, book, date, royalties):
        return self.sign_contract(book, date, royalties)

    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book is self]

    def authors(self):
        authors = []
        for contract in self.contracts():
            if contract.author not in authors:
                authors.append(contract.author)
        return authors


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError("author must be an Author")
        self._author = author

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise TypeError("book must be a Book")
        self._book = book

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        self._date = date

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        if type(royalties) != int:
            raise TypeError("royalties must be an integer")
        self._royalties = royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
