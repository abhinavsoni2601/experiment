list1=[]
while(True):
    for x in range(0,25):
        inp=input("enter the absentee")
        list1.append(inp)
        if not inp:
            break
    break
with open("absentee.txt","w") as file1:
    for x in list1:
        file1.write(x)
file2=open("absentee.txt","r")        
print(file2.read())        