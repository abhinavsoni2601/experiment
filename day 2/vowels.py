a="alabama california oklahoma florida"
s=""
for x in a:
    if(x=="a"or x=="e" or x=="i" or x=="o" or x=="u"):
        continue
    else: 
        s=s+x
list2=s.split()
print(list2)
       
        