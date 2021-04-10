from typing import Optional
from fastapi import FastAPI
from maths import factorial


app = FastAPI()


@app.get("/testing")

def testing():
    return factorial(5)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/demo")
def demo():
    return {"This is ":"Demo"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/fib")
def fib(n):
    n=5
    return round((1.618034**n - (-0.618034)**n)/2.236068)



