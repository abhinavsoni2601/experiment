import mysql.connector 
from pandas import DataFrame
conn = mysql.connector.connect(user='gouravs785', password='@143lovejio',
                              host='db4free.net', database = 'db_kisikanhi')

c = conn.cursor()
c.execute("DROP Table bid;")

c.execute ("""CREATE TABLE bid(
          bidno TEXT,
          items  TEXT,
          quantity TEXT,
          n_addr TEXT,
          start_d TEXT,
          end_d TEXT
          )""")

c.execute("INSERT INTO bid VALUES ('1','coolers','3','Department of defence','12-12-2018','15-7-2019')")
c.execute("INSERT INTO bid VALUES ('2','fans','15','Department of finance','12-1-2019','15-7-2019')")
c.execute("INSERT INTO bid VALUES ('3','rafale','24','Indian Air Force','15-7-2016','15-7-2017')")
c.execute("INSERT INTO bid VALUES ('4','apache','15','Indian Air Force','15-7-2016','15-10-2016')")
c.execute("INSERT INTO bid VALUES ('5','s-400','2','DRDO','12-4-2018','12-4-2018')")


c.execute("SELECT * FROM bid")
df = DataFrame(c.fetchall())  
df.columns = ["NO","ItEMS","Quantity","Organization","start","end"]