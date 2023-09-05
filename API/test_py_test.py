import pytest

# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
# def test_eval(test_input, expected):
@pytest.mark.parametrize("first_num,second_num,expected_sum", [(1, 2, 3), (-2, -2, -4), (5, 5, 11)])
def test_check_sum_test(first_num, second_num, expected_sum):
    assert custom_sum(first_num, second_num) == expected_sum


def custom_sum(first_num, second_num):
    return first_num + second_num
