
dict1={"letter":0,"digit":0}
inp=input("enter the string with digits and letters")
for x in inp:
    if x ==" ":
        continue
    elif x.isalpha():
        dict1["letter"]+=1
    else:
        dict1["digit"]+=1

dict1.items()
    
