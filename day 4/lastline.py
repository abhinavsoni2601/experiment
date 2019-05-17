
inp=input("enter the file name")
per=input("enter the permission")
file1=open(inp,per)
list1=file1.readlines()
print(list1[-1])