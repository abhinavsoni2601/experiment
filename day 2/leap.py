a=int(input("enter the leap year"))
print (a)
type(a)
def leap (ab) : 
    if (a%400==0):
        return True
    elif(a%4==0 and a%100!=0) :
        return True
    else:
        return False

leap(a)