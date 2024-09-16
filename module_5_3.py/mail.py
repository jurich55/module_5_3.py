
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return str(f'Название: {self.name}, количество этажей: {self.number_of_floors}')

    def __eq__(self, other):
        if not isinstance(other, House):
            print(f"другой {other} не типа Хаус")
        else:
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if not isinstance(other, House):
            print(f"другой {other} не типа Хаус")
        else:
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if not isinstance(other, House):
            print(f"другой {other} не типа Хаус")
        else:
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if not isinstance(other, House):
            print(f"другой {other} не типа Хаус")
        else:
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if not isinstance(other, House):
            print(f"другой {other} не типа Хаус")
        else:
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if not isinstance(other, House):
            print(f"другой {other} не типа Хаус")
        else:
            return self.number_of_floors != other.number_of_floors
    
    def __add__(self, value):
        if isinstance(value, int):   # если value - число,... его и прибавляем
            self.number_of_floors = self.number_of_floors + value
        return self

    def __iadd__(self, value):
        if isinstance(value, int):   # если value - число,... его и прибавляем
            self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        if isinstance(value, int):   # если value - число,... его и прибавляем
            self.number_of_floors = self.number_of_floors + value
        return self



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(str(h1))
print(str(h2))

print(h1 == h2)    # False -> 10 != 20

h1 = h1 + 10       # __add__  -> ЖК 'Эльбрус', количество этажей: 20
print(h1)
print(h1 == h2)    # True  -> 20 = 20

h1 += 10           # __iadd__  -> ЖК 'Эльбрус', количество этажей: 30
print(h1)

h2 = 10 + h2       # __radd_   -> ЖК 'Акация', количество этажей: 30
print(h2)

print(h1 < h2)     # __lt__      False  -> 30 = 30
print(h1 <= h2)    # __le__      True   -> 30 = 30
print(h1 > h2)     # __gt__      False  -> 30 = 30
print(h1 >= h2)    # __ge__      True   -> 30 = 30
print(h1 != h2)    # __ne__      False  -> 30 = 30