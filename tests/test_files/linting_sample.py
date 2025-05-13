#!/usr/bin/env python3
"""
A sample file with various linting issues for testing ruff output parsing.
"""

import os
import sys
import json
import datetime
import time
import math  # Multiple unused imports

from collections import defaultdict, Counter, OrderedDict  # More unused imports

# Variable assigned but never used
unused_var = 100

# Constant variable not in uppercase
constant_pi = 3.14159

# Multiple imports on one line
import logging, random, re

# Using 'is' with literals
x = 5
if x is 5:  # Should use == for value comparison
    pass

# Using mutable default argument
def func_with_mutable_default(a, items=[]):
    items.append(a)
    return items

# Undefined name
def undefined_name_function():
    # The variable 'undefined_var' is not defined
    return undefined_var * 2

# Format string without any placeholders
f_string_no_placeholders = f"This string has no placeholders"

# Shadowing a built-in name
def list(items):
    # Shadows the built-in 'list'
    return items

# Line too long
very_long_line = "This is a very long line that exceeds the default line length limit so that ruff will report it as an error in linting output"

# Duplicate key in dict
duplicate_keys = {
    "key1": "value1",
    "key2": "value2",
    "key1": "value3"  # Duplicate key
}

# Ambiguous variable name
l = [1, 2, 3]  # Single letter variable name that looks like '1'
O = 5  # Upper case 'O' looks like '0'

# Access to protected member
class SampleClass:
    def __init__(self):
        self._protected = "internal use only"

instance = SampleClass()
protected_value = instance._protected  # Accessing protected member

# Using a bare except
try:
    risky_operation = 1 / 0
except:  # Too broad exception clause
    pass

# Class without docstring
class UndocumentedClass:
    def __init__(self):
        self.value = 10
        
    def method(self):
        return self.value * 2

# Import not at top of file
import csv  # Should be at the top of the file

# Unreachable code
def unreachable():
    return "early return"
    print("This will never execute")  # Unreachable code

# Too complex function (McCabe complexity)
def complex_function(n):
    result = 0
    for i in range(n):
        if i % 2 == 0:
            if i % 3 == 0:
                result += i * 3
            else:
                result += i * 2
        elif i % 3 == 0:
            if i % 5 == 0:
                result += i * 5
            else:
                result += i * 3
        elif i % 5 == 0:
            result += i * 5
        elif i % 7 == 0:
            result += i * 7
        else:
            result += 1
    return result

# Function with too many arguments
def too_many_args(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6 + arg7 + arg8

if __name__ == "__main__":
    print("This file is intentionally full of linting issues for testing")