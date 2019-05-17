import re
result=[]
inp="gourav@gmail.com abhinav@gmail.com raghu@ rehman@yahoo ranky@reat.co lara@hackerrank.com brian-23@hackerrank.com britts_54@hackerrank.com"

list1=inp.split()
for x in list1:
    result.append(re.findall(r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$',x))
print(result)