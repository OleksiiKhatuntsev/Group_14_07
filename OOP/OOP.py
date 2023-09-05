import math

#
# def get_sum(first_num, second_number):
#     result = first_num + second_number
#     return result
#
#asd
#
# print(get_sum(1,2))
# with open("result.txt", "x") as file:
#     file.write(get_sum(1,2).__str__())


class Round:
    def __init__(self, radius):
        if radius < 0:
            raise Exception(f"its can't be a round with radius < 0, your radius - {radius}")
        self.__radius = radius # self._Round__radius   instance._class-name__private-attribute


    def get_perimeter(self):
        return math.pi * self.__radius * 2


round = Round(-5)
print(round.get_perimeter())
round.radius = -5
round.__radius = -5
round._Round__radius = -5
print(round.get_perimeter())

# DRY - Don't Repeat Youself
# YAGNI - You ain't gonna need it
# KISS - keep It Simple, Stupid
