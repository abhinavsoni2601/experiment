list1=[]
str1=""
dict1={}
file1=open("romeo.txt","r")
list1=file1.readlines()
for x in list1:
    str1=str1+x
list2=str1.split()
print(list2)
for y in list2:
    if (y not in dict1.keys()):
        dict1[y]=1
    else:
        dict1[y]+=1
print(dict1.items())

