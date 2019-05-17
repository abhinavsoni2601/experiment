list1=[12,23,454,123,56]

for x in list1:
    if(x>0):
        flag=True
    else:
        flag =False
        break
        
if(flag == True):
    for x in list1:
        a=str(x)
        if(a==a[::-1]):
            print("true")
        else:
            continue
else:
    print("false")
        
        