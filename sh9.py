list1=[]
n=0
while n<6:
    a=int(input("enter a number"))
    list1.append(a)
    n=n+1
print(list1)
s=0
for b in list1:
    s=s+b
print("the sum is ", s)      
