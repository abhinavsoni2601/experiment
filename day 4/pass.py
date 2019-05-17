file1=open("passwd","r")
str1=""
dict1={}
list1= file1.readlines()
for x in list1:
    str1=str1+x
    list2=str1.split(":")
    dict1[list2[0]]=list2[2]
    str1=""
print(sorted(dict1.items()))