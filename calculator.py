# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 14:17:25 2025

@author: jdev1
"""
import math

history_list =  []

def add(x,y):
    string_ver = "add( " + str(x) + "," + str(y) + ") equals: " + str(x+y)  
    history_list.append(string_ver )
    return x + y

def minus(x,y):
    string_ver = "minus( " + str(x) + "," + str(y) + ") equals: " + str(x-y)  
    history_list.append(string_ver )
    return x - y

def multiply(x,y):
    string_ver = "multiply( " + str(x) + "," + str(y) + ") equals: " + str(x*y)  
    history_list.append(string_ver )
    return x * y

def powering(x,y):
    string_ver = "powering( " + str(x) + "," + str(y) + ") equals: " + str(x**y)  
    history_list.append(string_ver )
    return x ** y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    result = x / y
    history_list.append(f"divide({x}, {y}) equals: {result}")
    return result
   
def squareRoot(x):
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    result = math.sqrt(x)
    string_ver = f"square root({x}) equals: {result}"
    history_list.append(string_ver)
    return result
    
def history():
    for element in history_list:
        print(element)

def clear_history():
    history_list.clear()
        