import csv
dict1={}
file1=open("passwd","r")
str1=file1.read()
list1=str1.split("\n")
print(list1)
for x in list1:
    str2=x
    list2=x.split(":")
    dict1[list2[0]]=list2[2]
    str2=""
with open("passwd.csv",mode="w")as file2:
    writer=csv.writer(file2,delimiter=",")
    for q,w in dict1.items():
        writer.writerow([q,w])
with open("passwd.csv",mode="r")as file3:
    reader=csv.reader(file3,delimiter=",")
    for y in reader:
        print (y)