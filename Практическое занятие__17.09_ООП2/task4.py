class Book:
    def __init__(self, title, author, year, isbn, pages):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Заголовок должен быть непустой строкой")
        if not isinstance(author, str) or not author.strip():
            raise ValueError("Автор должен быть непустой строкой")
        if not isinstance(isbn, str) or not isbn.strip():
            raise ValueError("ISBN должен быть непустой строкой")
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Год издания должен быть положительным целым числом")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.pages = pages

    def __str__(self):
        return f"{self.author} — '{self.title}' ({self.year})"

    def __repr__(self):
        return (f"Book(title={self.title!r}, author={self.author!r}, year={self.year}, "
                f"isbn={self.isbn!r}, pages={self.pages})")

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        
        return self.author == other.author and self.title == other.title

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        if self.author != other.author:
            return self.author < other.author
        return self.title < other.title

    def __len__(self):
        return self.pages


book = Book("Война и мир", "Толстой", 1869, "978-5-389-07455-3", 1225)
print(len(book))
print(book)
print(book == Book("Война и мир", "Толстой", 1869, "111-1-111-11111-1", 1225))
print(repr(book))
