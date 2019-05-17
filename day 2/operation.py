a=input("enter the numbers using spaces")
list1=a.split()
list2=[]
list3=[]
b=0
for x in list1:
    list2.append(int(x))
for y in list2:
    b=b+y
print("sum =" ,b)
print("max is ",max(list2))
print("min is ", min(list2))
for x in list2:
    if(x not in list3):
        list3.append(x)
print(list3)
    

