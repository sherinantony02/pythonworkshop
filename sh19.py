list= [32,45,25,15]
small=list[0]
for i in range(len(list)):
    if (small>list[i]):
        small=list[i]
print("largest number is:",small)
