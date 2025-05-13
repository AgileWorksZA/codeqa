def simple_function():
    return "Hello World"

def medium_complexity(x, y):
    if x > 10:
        if y > 10:
            return x * y
        else:
            return x + y
    else:
        if y > 5:
            return x - y
        else:
            return x / y if y != 0 else 0

def high_complexity(numbers):
    result = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            if numbers[i] % 3 == 0:
                result += numbers[i] * 2
            else:
                result += numbers[i]
        else:
            if numbers[i] % 5 == 0:
                result -= numbers[i]
            elif numbers[i] % 7 == 0:
                result += numbers[i] // 2
            else:
                result += 1
    return result

class ComplexClass:
    def __init__(self, value):
        self.value = value
    
    def process(self, data):
        if self.value > 100:
            return [x * 2 for x in data if x > 10]
        else:
            result = []
            for x in data:
                if x < 0:
                    result.append(-x)
                elif x < 10:
                    result.append(x * x)
                else:
                    result.append(x)
            return result