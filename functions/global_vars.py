# variable_not_in_function = 1
#
#
# def sum_two_numbers(first_number: int, second_number: int | float) -> float | int:
#     return "first_number + second_number"
#
# def myfunc():
#     global x
#     x = 5
#     def myfunc1():
#       x = "John"
#       def myfunc2():
#         nonlocal x
#         x = "hello"
#       myfunc2()
#       return x
#
# # print(myfunc1())
# def change_int_to_string():
#     global variable_not_in_function
#     variable_not_in_function = "qwe"
#     return variable_not_in_function
#
#
# change_int_to_string()
# print(sum_two_numbers("qwe", 1))
# print(help(sum_two_numbers))
# print(myfunc())
#
#
# def wait_for_user_input_qwe():
#     text = input("Input qwe: ")
#     if text == "qwe":
#         return text
#     else:
#         return wait_for_user_input_qwe()
#
# def wait_for_user_input_qwe_loop():
#     while True:
#         text = input("Input qwe: ")
#         if text == "qwe":
#             return text
# import sys
#
#
# def add_two_to_number(number: int):
#     print(number)
#     if (number == 500):
#         return number
#     else:
#         number += 2
#         add_two_to_number(number)
# sys.setrecursionlimit(100500)
# # wait_for_user_input_qwe()
# # wait_for_user_input_qwe_loop()
# add_two_to_number(499)
#
# def add_ten_to_number(number):
#     return number + 10
#
# add_ten_to_num = lambda a, b, c: print(a + b + c)
#
#
# add_ten_to_num(1,2,3)
# print(add_ten_to_number(0))

# def is_even_number(list_of_nums):
#     result = []
#     for num in list_of_nums:
#         if num % 2 == 0:
#             result.append(num)
#
#     return result

# print(is_even_number(range(1,5)))
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #
# # even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 5)))
# # even_numbers = [lambda x: x if x % 2 == 0 else 0]
# # print(even_numbers())
# #
# # even_numbers = [x for x in my_list if x % 2 == 0]
#
# result = []
# for x in my_list:
#
#     if x % 2 == 0:
#         result.append(x)
#
# max = lambda a, b: a if (a > b) else b
#
# print(even_numbers)
#
#
# 1, 1, 2, 3, 5, 8, 13, 21, 34
