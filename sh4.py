x =int(input("enter a number"))
y =int(input("enter 2nd number"))
operation =input("enter the operand")
result="0"
if operation=="+":
    result =x+y
elif operation=="-":
    result =x-y
elif operation=="/":
    result =x/y
else:
    print("you entered a invalid operation")
print("the result is", result) 
