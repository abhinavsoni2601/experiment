from functools import reduce 
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
list1=list(filter(lambda x:True if "height" in x else False ,people))
list2=list(map(lambda x: x['height'],list1))
list3=reduce(lambda x,y: x+y,list2)
