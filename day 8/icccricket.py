from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from collections import OrderedDict
url=" https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
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

col_name=["team","number_of_match","points","rating"]
col_data= OrderedDict(zip(col_name,[name,match,pt,rating]))
df = pd.DataFrame(col_data) 

