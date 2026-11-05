import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на 0"
    return a / b

def modulo(a, b):
    if b == 0:
        return "Ошибка: деление на 0"
    return a % b

def degree(a, b):
    return a ** b

def Sin(a):
    return math.sin(math.radians(a))
    
def Cos(a):
    return math.cos(math.radians(a))
