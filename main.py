from typing import Optional
from fastapi import FastAPI
from maths import fibonnaci,fibo_recursive,factorial
from strings import len_string,len_string_manual

salesassist_app = FastAPI()

#Fibonnaci using O(1)
@salesassist_app.get("/fibo")
def fibo():
    return fibonnaci(9)

#fibonnaci using recursion
@salesassist_app.get("/fibo/recursive")
def fibo_recursion():
    return fibo_recursive(9)


#factorial of a number
@salesassist_app.get("/factorial")
def factorial_num():
    return factorial(5)


#len of a sting
@salesassist_app.get("/len_string")
def len_of_string():
    return len_string("Shivam")




