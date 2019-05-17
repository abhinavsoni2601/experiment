import pandas as pd
from selenium import webdriver
from collections import OrderedDict
url="https://bidplus.gem.gov.in/bidlists"
driver = webdriver.Chrome(r"D:\forks\day 8\chromedriver")
driver.get(url)
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
for x in range(1,11):
    inp='//*[@id="pagi_content"]/div['+ str(x)+']/div[1]/p[1]/a'
    inp1='//*[@id="pagi_content"]/div['+str(x)+']/div[2]/p[1]/span'
    inp2='//*[@id="pagi_content"]/div['+str(x)+']/div[2]/p[2]/span'
    inp3='//*[@id="pagi_content"]/div['+str(x)+']/div[3]/p[2]'
    inp4='//*[@id="pagi_content"]/div['+str(x)+']/div[4]/p[1]/span'
    inp5='//*[@id="pagi_content"]/div['+str(x)+']/div[4]/p[2]/span'
    my_data=driver.find_element_by_xpath(inp).text
    my_data1=driver.find_element_by_xpath(inp1).text
    my_data2=driver.find_element_by_xpath(inp2).text
    my_data3=driver.find_element_by_xpath(inp3).text
    my_data4=driver.find_element_by_xpath(inp4).text
    my_data5=driver.find_element_by_xpath(inp5).text
    list1.append(my_data)
    list2.append(my_data1)
    list3.append(my_data2)
    list4.append(my_data3)
    list5.append(my_data4)
    list6.append(my_data5)
    
col_name = ["company","item","quantity","addr","start","end"]
col_data = OrderedDict(zip(col_name,[list1,list2,list3,list4,list5,list6]))
df = pd.DataFrame(col_data)
