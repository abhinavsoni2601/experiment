import re
list2=[]
inp="4123456789123456 5123-4567-8912-3456 61234-567-8912-3456 4123356789123456 5133-3367 -8912-3456 5123 - 3567 - 8912 - 3456"
list1=inp.split()
for x in list1:
    list2.append(re.findall(r"^[456]{1}\d{3}-\d{4}-\d{4}-\d{4}",x))

print(list2)