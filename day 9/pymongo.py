import pymongo
from pandas import DataFrame
client = pymongo.MongoClient("mongodb://gouravs785:%40143lovejio@cluster0-shard-00-00-xdvjd.mongodb.net:27017,cluster0-shard-00-01-xdvjd.mongodb.net:27017,cluster0-shard-00-02-xdvjd.mongodb.net:27017/test?ssl=true&replicaSet=cluster0-shard-0&authSource=admin&retryWrites=true")
mydb = client.university

def add_student(name,age,roll,branch):
    mydb.students.insert_one(
            {
            "name" : name,
            "age" : age,
            "roll" : roll,
            "branch" : branch
            })
    return "student added successfully"         
                    
add_student('GOURAV',21, 63, 'CSE')
add_student('ABHINAV',21,5, 'CSE')
add_student('DEEP',22, 100, 'IT')
add_student('ASKHAY',20,3,'ECE')
add_student('DIGVENDRA',18,55,'HM')

def fetch_all_student():
    user = mydb.students.find()
    for i in user:
        print (i)
fetch_all_student()