import string
a="The quick brown fox jumps over the lazy dog"
e=a.lower()
b=list(string.ascii_lowercase)
c=""
for x in e:
    if (x in b and x not in c):
        c=c+x
    else: 
        continue
   
d=sorted(c)
if(b==d):
    print("true")
else:
    print("false")
    
