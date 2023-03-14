
file=open("file.txt", 'r')
contents=file.readlines()
for a in contents:
    if int(a.strip()) %2==0:
        print(a.strip())
file.close()
