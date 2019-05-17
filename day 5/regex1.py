import re
inp="-12.5"
result=re.search(r'^[+-]?\d+\.\d+$',inp)
print(result)