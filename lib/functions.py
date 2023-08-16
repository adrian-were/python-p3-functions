#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    pass

def greet(name="Naureen"):
    print(f"Hello, {name}!")
    pass

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    pass

def add(num1, num2):
    return num1 + num2
    pass

def halve(number):
    if type(number) not in (int, float):
        return None
    return number / 2
