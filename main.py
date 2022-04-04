def count_vowels(text):
    count = 0
    for char in text:
        if char in "AaEeIiOoUu":
            count += 1
    if count == 0:
        return 42
    return count

print(count_vowels("thereforE"))


def hamming(text1, text2):
    distance = 0
    A = len(text1)
    B = len(text2)
    if A == B:
        for i in range(A):
            if text1[i] != text2[i]:
                distance += 1
        return distance
    if A != B:
        return 0


print(hamming("Hund", "Mund"))


class Vehicle:
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type


class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)
        self.doors = doors

    def __str__(self):
        return f"Color: {self.color}, Fuel Type: {self.fuel_type}, Doors: {self.doors}"

class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return f"Color: {self.color}, Fuel Type: {self.fuel_type}, Passengers: {self.passengers}"


car1 = Car("green", "gasoline", 4)
bus1 = Bus("silver", "diesel", 10)

print(car1)
print(bus1)

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return f"{self.name}, {self.author}"


book1 = Book("Dune", "Frank Herbert")
book2 = Book("Crescent City", "Sarah J. Maas")
print(book1)


class Bookshelf:
    def add_book_list(self, books):
        self.books = books
        book_list = []
        for i in books:
            if books == books(Book):
                book_list.append(i)
            print(book_list)

