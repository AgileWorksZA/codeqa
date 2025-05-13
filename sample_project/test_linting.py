import os
import sys
import datetime
import json

unused_var = "this is unused"

def hello_world():
    """Say hello."""
    print ("Hello World!")

def calculate_something(x, y):
    """Calculate something."""
    a = x + y 
    return a

# This is too complex according to most linters
def complex_function(a, b, c, d, e, f):
    """Do complex stuff."""
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    if e > 0:
                        if f > 0:
                            return "all positive"
                        else:
                            return "f is negative"
                    else:
                        return "e is negative"
                else:
                    return "d is negative" 
            else:
                return "c is negative"
        else:
            return "b is negative"
    else:
        return "a is negative"