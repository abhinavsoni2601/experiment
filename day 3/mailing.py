list1=["xyz.@gmail.com","abc@gmail.com","bcc@gmail.com","aaa@gmail.com","222@gmail.com"]
list2=["xyz.@gmail.com","abc@gmail.com","dde@gmail.com","qqq@gaml.com"]
s2=set(list1)
s3=set(list2)
s1=s2.difference(s3)
print(s1)