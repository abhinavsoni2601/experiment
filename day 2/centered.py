a=input("enter the number with spaces")
list1=a.split()
list2=[]
sum1=0
for x in list1:
    list2.append(int(x))
    
list2.pop(list2.index(max(list2)))
list2.pop(list2.index(min(list2)))

for y in list2:
    sum1=sum1+y
d=int(sum1/len(list2))
print(d)