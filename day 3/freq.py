dict1={}
inp=input("enter the string ")
for x in inp:
    if(x not in dict1.keys()):
        dict1[x]=1
    else:
        dict1[x]+=1
dict1.items()
    