from collections import OrderedDict
dict1=OrderedDict()
dict2=OrderedDict()
while True:
    inp=input("enter the items and values")
    if not inp:
        break
    inp=inp.split()
    k=''.join(inp[:-1])
    if k in dict1.keys():
        dict1[k]+=int(inp[-1])
    else:
        dict1[k]=int(inp[-1])
dict1.items()    
    
    
    