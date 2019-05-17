import random
list1=['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
list3=list(map(lambda list1: random.choice(code_names),list1))