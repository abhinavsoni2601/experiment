from functools import reduce

list1=[[34587,"Learning Python", "Mark Lutz" ,4,40.95],
    [98762, "Programming Python", "Mark Lutz", 5, 56.80],
    [77226, "Head First Python", "Paul Barry", 3, 32.95],
    [88112, "Einführung in Python3", "Bernd Klein",3,24.99]]
list2=[]
for x in list1:
     sum1=x[3]*x[4]
     list2.append((x[0],sum1))
print(list2)

list3=list(map(lambda x:(x[0],x[3]*x[4]) if x[3]*x[4]>100 else (x[0],x[3]*x[4]+10),list1))