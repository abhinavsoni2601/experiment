list1=[12,24,35,24,88,120,155,88,120,155]
list2=[]
for x in list1:
    while x not in list2:
        list2.append(x)
print(list2)