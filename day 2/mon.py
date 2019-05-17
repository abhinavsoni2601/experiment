list1=["jan","mar","may","july","aug","oct","dec"]
list2=["apr","june","aug","sep","nov"]
list3=["feb"]

a=input("enter the month")
b=int(input("enter the year"))

if(a in list1):
    print("31")
elif(a in list2):
    print("30")
elif(a in list3):
    if (b%400==0):
        print ("29")
    elif(b%4==0 and b%100!=0):
        print ("29")
    else:
        print ("28")
            
        