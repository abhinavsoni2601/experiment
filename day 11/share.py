from bs4 import BeautifulSoup as bs
from selenium import webdriver
import matplotlib.pyplot as plt
lsstate=[]
lsshare=[]
url="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
browser=webdriver.Chrome("chromedriver.exe")
browser.get(url)
for x in range(1,7):
    state=browser.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(x)+']/td[2]').text.strip()
    share=browser.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(x)+']/td[5]').text.strip()
    lsstate.append(state)
    lsshare.append(share)
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.2, 0, 0, 0 ,0 , 0)
plt.pie(lsshare, explode=explode, labels=lsstate, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)
plt.savefig("share.jpg")