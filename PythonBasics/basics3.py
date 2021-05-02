# syntax for function is as follows
# def func_name(parameter):
#     body

def printhello():
    print("Hello")

printhello()

def printhi(name="Rahul"):
    print("Hi, "+name)

printhi("Raghav")
printhi()

def sum(a,b,c):
    print(a+b+c)

sum(10,20,30)

def returnSum(a,b):
    """this is the function to return the sum of two numbers"""
    return(a+b)

x = returnSum(10,20)
print(x)