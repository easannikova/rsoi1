import unittest

from fib_summaraiser import sum_fibonachi

#comment1
def test_fibonachi_sum():
    res1 = sum_fibonachi(0)
    assert res1 == 0
    res2 = sum_fibonachi(2)
    assert res2 == 2
    res3 = sum_fibonachi(6)
    assert res3 == 20
    res4 = sum_fibonachi(15)
    assert res4 == 1596
