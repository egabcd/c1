
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if a == 0:
        raise ValueError("Divide by zerro")
    else:
        return a/b
