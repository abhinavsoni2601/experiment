def brick (sm,lg,tg):
    flag=0
    if(tg<sm):
       flag=1
       return flag
    elif (tg%5==0 and int(tg/5)<=lg):
        flag=1
        return flag
    else:
        temp=5*lg
        if(tg-temp<sm):
            flag =1
            return flag
        else:
            return 0
          
      
     
a=input("enter the no of small brick , big brick , target")
list2=[]
list1=a.split()
for x in list1:
    list2.append(int(x))
b=list2.pop(0)
c=list2.pop(0)
d=list2.pop(0)
print(b,c,d)
e=brick(b,c,d)
if(e==1):
    print("true")
else:
    print("false")
