from fastapi import FastAPI
from maths import fibonnaci,fibo_recursive,factorial
from strings import len_string,len_string_manual,string_gen

salesassist_app = FastAPI()

#Fibonnaci using O(1)
@salesassist_app.get("/fibo/{number}")
def fibo(number: int):
    return fibonnaci(number)

#fibonnaci using recursion
@salesassist_app.get("/fibo/recursive/{number}")
def fibo_recursion(number: int):
    return fibo_recursive(number)


#factorial of a number
@salesassist_app.get("/factorial/{number}")
def factorial_num(number: int):
    return factorial(number)


#len of a sting
@salesassist_app.get("/len_string/{string}")
def len_of_string(string: str):
    return len_string(string)


#generate and return a string of a given length of a chosen character as input

@salesassist_app.get("/gen_string/{len}{string}")

def string_generation(len: int, string: str):
    return string_gen(len, string)
