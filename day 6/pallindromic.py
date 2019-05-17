inp=input("enter the numbers with space")
list1=inp.split()
list2=[]
for x in list1:
    if(x==x[::-1]):
        list2.append( True)
    else:
        list2.append(False)
print(any(list2))