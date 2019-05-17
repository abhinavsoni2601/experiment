a=input("enter the number with spaces")
list1=a.split()
list2=[]
flag=0
flag1 =0
sum1=0
for x in list1:
    list2.append(int(x))
for y in list2:
    flag=y
    if(flag==13 or flag1==1):
        if(flag1==1):
            flag1=0
            continue
        flag1=1
        continue
    else:
        sum1=sum1+y
print(sum1)
