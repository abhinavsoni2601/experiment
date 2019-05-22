from collections import Counter
import numpy as np
x=np.random.randint(5,15,40)
count=Counter(x)
dict1={}
for item in x:
    if (item not in dict1.keys()):
        dict1[item]=1
    else:
        dict1[item]+=1