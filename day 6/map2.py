names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print (names)
names = ['Mary', 'Isla', 'Sam']

list3=list(map(lambda x:hash(x),names))