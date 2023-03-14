#functions
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
x=int(input("enter a number:"))
y=int(input("enter a number:"))
operation=input("enter a operation:")
if operation=="+":
    print(add(x,y))
else:
    print(sub(x,y))
