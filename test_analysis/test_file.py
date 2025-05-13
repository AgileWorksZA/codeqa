import os, sys, math

def complex_function(n):
    result = 0
    for i in range(n):
        if i % 2 == 0:
            result += i
        elif i % 3 == 0:
            result += i * 2
        elif i % 5 == 0:
            result += i * 3
        else:
            result += 1
    return result

def simple_function(x):
    return x * 2

class TestClass:
    def __init__(self, value):
        self.value = value
    
    def complex_method(self, n):
        result = 0
        for i in range(n):
            if i % 2 == 0:
                result += i
            else:
                result -= i
        return result
