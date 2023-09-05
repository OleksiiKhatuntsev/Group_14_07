def parametrized_decorator(n):
    def first_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"FIRST_IN {n}")
            func(*args, **kwargs)
            print(f"FIRST_OUT {n}")
        return wrapper
    return first_decorator

@parametrized_decorator(5)
def print_hello(word_to_print):
    print(word_to_print)

print_hello("NE HELLO")
# def second_decorator(func):
#     def wrapper():
#         print("SECOND_IN")
#         func()
#         print("SECOND_OUT")
#
#     return wrapper


# @first_decorator
# def print_not_hello():
#     print("NOT HELLO")



# @second_decorator

# print_not_hello()

# def repeat_n_times(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator

# Usage
# @repeat_n_times(3)  # This will repeat the decorated function 3 times
# def greet(name):
#     print(f"Hello, {name}!")
#
# greet("Alice")

