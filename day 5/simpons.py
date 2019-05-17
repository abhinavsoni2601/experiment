list2=[]
file1=open("simpsons_phone_book.txt","r")
str1=file1.read()
list1=str1.split("\n")
import re
for x in list1:
    list2.append(re.findall("^[J|j]{1}[a-zA-Z ]*Neu",x))
print(list2)