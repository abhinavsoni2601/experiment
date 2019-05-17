str1=""
i=0
j=0
k=0
dict1={}
file1=open("new.txt","r")
str1=file1.read()
print(str1)
for x in str1:
    if(x=="\n"):
        continue
    i+=1
print("the number of charaters is ",i)
list1=str1.split()
for y in list1:
    j+=1
print("the number of words are : ",j)
list2=str1.split("\n")
for z in list2:
   k+=1
print("the number of lines are :",k)
s1=set(list1)
for q in s1:
    k+=1
print(k)