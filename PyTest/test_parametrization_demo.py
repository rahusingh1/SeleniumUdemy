import pytest

def sum(a,b):
    return a+b

@pytest.mark.parametrize("input1, input2, output",
                         [
                             (2,3,5),
                             (5,4,10),
                             (12,5,17)
                         ])
def test_sum_1(input1, input2, output):
    result = sum(input1,input2)
    assert result == output

# def test_sum_2():
#     result = sum(5,4)
#     assert result == 9
#
# def test_sum_3():
#     result = sum(12,5)
#     assert result == 17