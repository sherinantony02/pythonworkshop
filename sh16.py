file=open("file.txt",'r')
contents=file.read()
contents=contents.split(',')
#for a in contents:
 #   if int(a)%2==0:
  #      print(a)
filetowrite=open("write.txt",'w')
for a in contents:
     if int(a) %2==0:
       filetowrite.write(a)
       filetowrite.write("\n")
     print(a)
with open("write.txt",'r') as file2:
     print(file2.read())       
