import os
import sys

# Add the directory containing the file to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from OtherЕopicsTasks import adder

def test_adder():
    add_five = adder(5)
    assert add_five(10) == 15
    assert add_five(5) == 10
    assert add_five(0) == 5
    
def test_adder_with_zero():
    add_zero = adder(0)
    assert add_zero(10) == 10
    assert add_zero(5) == 5
    assert add_zero(0) == 0

def test_adder_negative_numbers():
    add_negative = adder(-5)
    assert add_negative(-10) == -15
    assert add_negative(-5) == -10
    assert add_negative(0) == -5



test_adder()

test_adder_with_zero()

test_adder_negative_numbers()