dict1={}
flag=0
while True:
    inp=input("enter keys with thier values")
    if not inp:
        break
    inp=inp.split()
    dict1[inp[0]]=inp[-1]
def teen(num):
    if(num in range(13,20)):
        if(num==15 or num==16):
            return num
        return 0
    else:
        return num    
    
for x in dict1.values():
    y=int(x)
    flag=flag+teen(y)
print(flag)