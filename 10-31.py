import pandas as pd
import matplotlib.pyplot as plt
# data={
#     "vardas":["Jonas","Maryte", "Arturas", "Migle", "Zose"],
#     "amzius":[25,45,30,12,65],
#     "miestas":["Klaipeda","Anyksciai", "Vilnius", "Plunge", "Vilnius"]
# }
#
#
# df=pd.DataFrame(data)
# vyresni_nei_25=df[df["amzius"]>25]
# grupavimas_pagal_miesta= df.groupby("miestas").size()
#
# df=df.sort_values(by="amzius",ascending=True)     #rusiuoja
# df=df.sort_values(by="amzius",ascending=False)
#
# # Pridesim nauja stulpeli, pridejimas prie jau esancios lenteles.Reiksmiu kiekis turi sutapti.
# df["darbo_stazas"]=[5,7,8,12,19]
# #
# # # norime istrinti stulpeli
# df.drop(columns=["darbo_stazas"],inplace=True)   # inplace nedaro veliau tarpo lenteleje
# print(df)
#
# eiluciu_sk=df.shape[0]
# stupeliu_sk=df.shape[1]
# print (f"Eiluciu skaisius {eiluciu_sk}, stulpeliu saicius  {stupeliu_sk}")

# df=pd.read_csv("Sales_Records.csv")   #funkcija nuskaityti csv faila
# df["Profit"]=df["Total Revenue"]-df["Total Cost"]   # sukureme nauja stulpeli profit ir suskaiciavom stulpeliu skirtuma
# #
# # df["Profit"]=df["Profit"].round(2)                  #suapvalinam atsakyma iki dvieju skaiciu po kablelio
#
# # # issaugojimas
# # df.to_csv("nauja lentele.csv", index=False)     # issaugom nauja lentele su profit stulpeliu
#
# # print("bendras pelnas",df["Profit"].sum(), df["Total Revenue"].sum(), df["Total Cost"].sum())
# df["Ship Date"]=pd.to_datetime(df["Ship Date"])          #teksto formatavimas i data
# df["Order Date"]=pd.to_datetime(df["Order Date"])
# df['Units Sold']=df['Units Sold'].astype(int)      #formatavimas is teksto i skaiciu
# #
# df["siunta uztruks"]=(df["Ship Date"]-df["Order Date"]).dt.days
# # print(df)
# # # tkriname ar visos eilutes uzpildytos ar nera tusciu reiksmiu
# # print(df.isnull().sum())
#
# # # surusiujam mazejimo tvarka
# # surusiuta = df.sort_values(by="Profit", ascending=False)
# # print(surusiuta)
#
# # df["margin_on_revenue"]= (df["Profit"]/df["Total Revenue"])*100
# # # df["margin_on_revenue"]= df["margin_on_revenue"].round(2).astype(str)+"%"   #parasymas su procento zenkliuku
# # df["margin_on_revenue"]= df["margin_on_revenue"].apply(lambda x:f"{x:.2f}%")    # su procentais kitas variantas
# #
# # print(df)
#
# # plt.figure(figsize=(10,7))     # histogramos dydis
# # plt.hist(df["Profit"],bins=10,edgecolor='black')
# # plt.title('Pelno histograma')
# # plt.xlabel('Pelnas')
# # plt.ylabel('Daznis')
# # plt.savefig("Histograma.png")   # sukuria grafiko paveiksleli
# # plt.show()
#
# # plt.bar(['Unit Price','Units Sold'],[df['Unit Price'].mean(),df['Units Sold'].mean()])
# # plt.title('Vidutine kaina')
# # plt.ylabel('kaina')
# # plt.show()
#
# plt.figure(figsize=(6,8))
# plt.hist(df["siunta uztruks"], bins=10,edgecolor='red')
# plt.title('Siunta uztruks')
# plt.ylabel('uzsakymu skaicius')
# plt.xlabel('dienos skirtumas')
# plt.show()




#  paememe orus savaites is meteo ir nubraizem diagrama
import requests
from bs4 import BeautifulSoup

import psycopg2




# url="http://www.meteo.lt/en/miestas?placeCode=Vilnius"
# response=requests.get(url)
# soup=BeautifulSoup(response.content,"html.parser")
# savaite=soup.find_all("span",class_="date")
# temperaturos=soup.find_all("span",class_="big up-from-zero")[1::2]
#
# isfiltruotos_dienos= [diena.get_text().split(",")[0] for diena in savaite]
# dienos_temperatura=[]
# for temperatura in temperaturos:
#     temp_text=temperatura.get_text().replace("°C","")
#     temp_value= int(temp_text[:-1])
#     dienos_temperatura.append(temp_value)
#
# interval=min(len(isfiltruotos_dienos),len(dienos_temperatura))
# print(dienos_temperatura)
# data={
#     "Diena":isfiltruotos_dienos,
#     "Temperatura":dienos_temperatura
#
#
# }
#
# df=pd.DataFrame(data)
# df.to_csv("temp.csv", index=False)
# print(df)


# plt.figure(figsize=(10,7))
# plt.bar(df["Diena"],df['Temperatura'])   #pridejus mean gauname vidutine temp
# plt.title('Temperaturos')
# plt.ylabel('Diena')
# plt.show()

#
# plt.figure(figsize=(10,7))
# plt.bar(["Vidutine temp"],df['Temperatura'].mean())
# plt.title('Temperaturos')
# plt.ylabel('Diena')
# plt.show()
#
# print(df["Temperatura"].mean().round(2))


#----------------------------------------------------------




url="http://www.meteo.lt/en/miestas?placeCode=Vilnius"
response=requests.get(url)
soup=BeautifulSoup(response.content,"html.parser")
savaite=soup.find_all("span",class_="date")
temperaturos=soup.find_all("span",class_="big up-from-zero")[::2]

isfiltruotos_dienos= [diena.get_text().split(",")[0] for diena in savaite]
dienos_temperatura=[]
for temperatura in temperaturos:
    temp_text=temperatura.get_text().replace("°C","")
    temp_value= int(temp_text[:-1])
    dienos_temperatura.append(temp_value)
nakties_temperatura=[]
for temperatura in temperaturos:
    temp_text=temperatura.get_text().replace("°C","")
    temp_value= int(temp_text[:-1])
    nakties_temperatura.append(temp_value)

dienos_interval=min(len(isfiltruotos_dienos),len(dienos_temperatura))
print(temperaturos)
data={
    "Diena":isfiltruotos_dienos,
    "Temperatura":dienos_temperatura


}

df=pd.DataFrame(data)


