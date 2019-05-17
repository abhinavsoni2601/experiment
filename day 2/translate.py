
a="This is fun"
b=""
c=a.lower()
for x in c:
    if(x!="a" and x!="e" and x!="i" and x!="o" and x!="u" and x!=" "):
        b=b+x
        b=b+"o"
        b=b+x
    else:
        b=b+x
print(b)
    
