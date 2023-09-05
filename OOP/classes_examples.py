# class Figure:
#     def __init__(self, radius, measure_of_length ):
#         self.measure_of_length = measure_of_length.upper()
#         self.radius = radius
#
#     def get_square(self):
#         pass
#
#     def get_perimeter(self):
#         pass
#
#
# class Square(Figure):
#     def __init__(self, side, measure_of_length, radius):
#         super().__init__(radius, measure_of_length)
#         self.side = side
#
#
#     def get_square(self):
#         return self.side ** 2
#
#     def get_perimeter(self):
#         return self.side * 4
#
#     def __str__(self):
#         return f"side - {self.side}{self.measure_of_length}"
#
# # square1 = Square(5, "sm")
# # square2 = Square(100500, "km")
# # print(f"{square1.side}{square1.measure_of_length}")
# # print(f"{square2.side}{square2.measure_of_length}")
# # print(square2 == square1)
# square = Square(5, "sm", 5)
# print(square.get_square())
# print(square.get_perimeter())
# print(square)
# # square1.radius = 1
# # asdlahkas.side = 10
# # print(asdlahkas.side)
# # print(square2.side)

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, heads_count, paw_count):
        self.heads_count = heads_count
        self.paw_count = paw_count

    @abstractmethod
    def get_a_battle_roar(self):
        pass

    @abstractmethod
    def bite(self):
        pass


class Cat(Animal):
    def __init__(self, heads_count, paw_count, tail, claws_count, cat_name):
        super().__init__(heads_count, paw_count)
        self.tail = tail
        self.claws_count = claws_count
        self.cat_name = cat_name


    def get_a_battle_roar(self):
        print("MEEEEEEEEEEO")


    def bite(self):
        print(f"{self.cat_name} with {self.tail} is doing a KUS`")


class Dog(Animal):
    def __init__(self, heads_count, paw_count, tail, claws_count, dog_name):
        super().__init__(heads_count, paw_count)
        self.tail = tail
        self.claws_count = claws_count
        self.dog_name = dog_name


    def get_a_battle_roar(self):
        print("ARRRRRRRRRRGH")


    def bite(self):
        print(f"{self.dog_name} with {self.tail} have cut your leg")

barsik = Cat(heads_count=1, paw_count=4, claws_count=18, tail="BIG PUSHISTY TAIL", cat_name="Barsik")
bobik = Dog(heads_count=1, paw_count=4, claws_count=18, tail="BIG PUSHISTY TAIL", dog_name="Bobik")
# barsik.bite()
# bobik.bite()


list_of_animals: [Animal] = [barsik, bobik]
for a in list_of_animals:
    a.bite()
    # print(a)

# b = Animal("asd", "asd")
# for animal in list_of_animals:
#     if animal.type == "Cat":
#         cat_doing_kus()
#     if animal.type == "Dog":
#         dog_doing_kus
