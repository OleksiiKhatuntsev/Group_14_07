# print(2/0)
# print("abc")
# print(int(input()))


try:
    result: int | str | None = print(int(input("Enter first number: "))/int(input("Enter second number: ")))
    raise TypeError
except ZeroDivisionError:
    print("Please, stop dividing by zero")
    # raise ZeroDivisionError(f"first number wa {first_num} and second was {second_num}")
except ValueError:
    result = "ads"
    print("You wrote not integer")
except:
    pass
finally:
    print("Finally")

print("abc")

# print(2/0)
# raise ZeroDivisionError
if "ф" in "фіва":
    assert False

def test_func():
    pass

if 1 == 1:
    pass
else:
    raise TypeError
