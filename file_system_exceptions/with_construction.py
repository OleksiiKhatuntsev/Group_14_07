# try:
#     file = open("test.txt")
#     print(file.readline())
# except UnicodeDecodeError:
#     pass
# finally:
#     file.close()

#
# with open("test.txt", "w") as file:
#     # print(file.readline())
#     file.write("asd\n")
#     file.write("My name Lesha\n")
# #
# with open("test2.txt", "w") as file:
#     # print(file.readline())
#     file.write("New data\n")
#
# with open("test.txt", "r") as file:
#     # print(file.readline())
#     result = file.readlines()
#
# print(result)
# result_array = []
# for r in result:
#     result_array.append(r.replace("\n", ''))
#
# print(result_array)

# from PIL import Image
with open("Diploma Front.jpg", "r+b") as file:
    print(file.read())


