import pytest
from series import fibonacci
from series import lucas
from series import sum_series

def test_fab1():
    actual=fibonacci(1)
    expected=1
    assert actual==expected

def test_fab2():
    actual=fibonacci(2)
    expected=1
    assert actual==expected

def test_fab3():
    actual=fibonacci(3)
    expected=2
    assert actual==expected
    
def test_fab6():
    actual=fibonacci(6)
    expected=8
    assert actual==expected

def test_lucas():
    actual=lucas(0)
    expected=2
    assert actual==expected

def test_lucas5():
    actual=lucas(5)
    expected=11
    assert actual==expected

def test_lucas8():
    actual=lucas(8)
    expected=47
    assert actual==expected

def test_Sum():
    actual=sum_series(4, 0, 1)
    expected=3
    assert actual==expected
    
def test_Sum6():
    actual= sum_series(5, 2, 1)
    expected=11
    assert actual==expected