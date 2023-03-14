file=open("file.txt",'r')
contents=file.read()
contents=contents.split(',')
for a in contents:
    if int(a)%2==0:
        print(a)
