def fibonnaci(n):
    return round((1.618034**n - (-0.618034)**n)/2.236068)
    # It will take O(1) time

def fibo_recursive(n):

    if(n<=0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibo_recursive(n-1)+fibo_recursive(n-2)


def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
