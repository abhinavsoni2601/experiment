file1=open("new.txt","r")
file2=open("new1.txt","w")
for x in file1:
    file2.write(x)
file2.close()
file2=open("new1.txt","r")
print(file2.read())

