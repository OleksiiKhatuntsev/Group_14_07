# def get_square(limit):
#     num = 1
#     while num <= limit:
#         yield num ** 2
#         num += 1

import datetime
import time

# @pytest.parametrize()
def get_test_mail(count):
    num = 1
    while num <= count:
        time.sleep(0.01)
        yield f"test_mail{datetime.datetime.now()}@gmail.com"
        num += 1

for el in get_test_mail(10):
    print(el)

# for el in get_square(5):
#     print(el)
#
# for el in "asd":
#     print(el)


# def read_lines_from_file(filename):
#     with open(filename, 'r') as file:
#         for line in file:
#             yield line.strip()
#
# # Provide the path to your text file
# file_path = 'test.txt'
#
# # Create a generator instance
# line_generator = read_lines_from_file(file_path)
#
# # Iterate through the lines using the generator
# for line in line_generator:
#     print(line)