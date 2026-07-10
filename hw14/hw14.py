class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    

v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v1)
print(v2)
print(v3)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self,other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author
    
book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')
print(book1 == book2)  # Output: True
print(book1 == book3)  # Output: False
    

class Car:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Brand არ უნდა იყოს ცარიელი")
        self._brand = value.strip()

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Model არ უნდა იყოს ცარიელი")
        self._model = value.strip()

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("Year უნდა იყოს მთელი რიცხვი")
        self._year = value

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

