import csv
list2=[]
list3=[]
list4=[]
dict1={}
sum1=0
list
with open("zoo.csv") as file1:
    reader=csv.reader(file1,delimiter=",")
    next(reader)
    for line in reader:
        list2.append(line)
print(list2)
for x in list2:
    if(x[0] not in dict1.keys()):
        dict1[x[0]]=int(x[2])
    else:
        dict1[x[0]]+=int(x[2])

print(dict1.items())