import mysql.connector 
from bs4 import BeautifulSoup as bs
import requests
from pandas import DataFrame
conn = mysql.connector.connect(user='gouravs785', password='@143lovejio',
                              host='db4free.net', database = 'db_kisikanhi')
url=" https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
c = conn.cursor()
c.execute ("""CREATE TABLE ICC(
          name TEXT,
          no_match  TEXT,
          pts TEXT,
          rating TEXT
          )""")

response=requests.get(url).text
soup=bs(response,"lxml")
my_table=soup.find("table",class_="table")
name=[]
match=[]
pt=[]
rating=[]
for x in my_table.findAll('tr'):
    cells=x.findAll('td')
    if(len(cells)==5):
        name.append(cells[1].text.strip())
        match.append(cells[2].text.strip())
        pt.append(cells[3].text.strip())
        rating.append(cells[4].text.strip())
        c.execute("INSERT INTO ICC VALUES (%s,%s,%s,%s)",(cells[1].text.strip(),str(cells[2].text.strip()),str(cells[3].text.strip()),cells[4].text.strip()))

c.execute("SELECT * FROM ICC")
df2 = DataFrame(c.fetchall())  
df2.columns = ["NAME","MATCH","POINT","RATING"]




 

