import sqlite3
from pandas import DataFrame
con=sqlite3.connect("university.db")
c=con.cursor()
c.execute("DROP TABLE db_university")
c.execute ("""CREATE TABLE db_university(
          Student_Name TEXT,
          Student_Age  INTEGER,
          Student_Roll_no INTEGER,
          Student_Branch TEXT
          )""")

c.execute("INSERT INTO db_university VALUES ('GOURAV',21, 63, 'CSE')")
c.execute("INSERT INTO db_university VALUES ('ABHINAV',21, 05, 'CSE')")
c.execute("INSERT INTO db_university VALUES ('DEEP',22, 100, 'IT')")
c.execute("INSERT INTO db_university VALUES ('ASKHAY',20,03,'ECE')")
c.execute("INSERT INTO db_university VALUES ('DIGVENDRA',18,55,'HM')")
c.execute("SELECT * FROM db_university")

df = DataFrame(c.fetchall())
df.columns = ["NAME","AGE","ROLL_NO","BRANCH"]
