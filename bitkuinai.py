import requests
from bs4 import BeautifulSoup
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}
url="https://www.coinbase.com/explore"
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.content,"html.parser")
content_block=soup.find_all("table",class_="cds-table-top40r1")
# lentele= soup.find('thead',class_="cds-table-header"")

data=[]

lentele= soup.find('table',class_="cds-table-top40r1")

if lentele:
    rows=lentele.find_all('tr')
    for row in rows:
        columns=row.find_all('td')
        if len(columns)>=8:
            player_data=[column.text.strip() for column in columns]
            data.append(player_data)

columns=["Name", "Price","Charts", "Change","Market cap","Volume (24h)","Supply"]
df = pd.DataFrame(data, columns = columns)
print(df)