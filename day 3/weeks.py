tup1=('Monday', 'Wednesday', 'Thursday', 'Saturday')
tup2=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
for x in tup2:
    if x not in tup1:
        tup1=tup1+(x,)
print(tup1)