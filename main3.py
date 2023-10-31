# with open("text.txt","w") as f:
#     content=f.write ("hello")

# with open("text.txt", "r") as f:
#     content=f.read()
# print(content)

# with open("text.txt", "a") as f:
#     content=f.write ("Labas krabas")

# susikuriam faila

import requests
from bs4 import BeautifulSoup

import psycopg2


# url="https://varle.lt"
# response=requests.get(url)
# print(response.status_code)

# 200 ok
# 301-302 file found/redirect http https:saugu protokola
# 403 forbidden
# 404 file not found
# 500 server error

# response=requests.get(url)
# print(response.content)

# url="https://aruodas.lt"
# response=requests.get(url)
# print(response.status_code)
#
# response=requests.get(url)
# print(response.content)
# url="https://aruodas.lt"
# response=requests.get(url)
# soup=BeautifulSoup(response.content,"html.parser")
#
# content_block=soup.find('div', class_="top-three-adverts__wrapper").text.strip()
# print (content_block)
# flat_date=[]
# def creat_and_insert_flats():
#     connection=psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="Aruodas",
#         user="postgres",
#         password="23duomenubaze23"
#     )
#     cursor=connection.cursor()
#
#     create_table_query="""
#     CREATE TABLE IF NOT EXISTS Aruodas_top(
#         id SERIAL primary key,
#         flat_title VARCHAR(300),
#         flat_price DECIMAL(10,2)
#     )"""
#
#     cursor.execute(create_table_query)
#     print ("Table create Successfully")
#
#     url="https://aruodas.lt"
#     response=requests.get(url)
#     soup=BeautifulSoup(response.content,"html.parser")
#
#     content_block=soup.select("div.top-three-adverts__wrapper div")
#     for content in content_block:
#         try:
#             flat_title=content.find("div", class_="top-three-adverts__advert__address").text.strip()
#             flat_price=content.find("span", class_="top-three-adverts__advert__price__price").text.strip()\
#                 .replace("€","").replace(" ", "").split(sep="-")[0]
#             insert_query="INSERT INTO aruodas_top(flat_title,flat_price) VALUES(%s,%s)"
#             cursor.execute(insert_query, (flat_title,flat_price))
#         except AttributeError:
#             continue
#     print("Flats inserted successfully")
#     connection.commit()
# creat_and_insert_flats()
#
#
#


# kuriame patys su kitais objektais:

flats_data = []
def create_and_insert_flats():
    #kuriam connectiona prie duomenu bezes:
    connection = psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "aruodas_informacija",
        user="postgres",
        password = "    "
    )

    cursor = connection.cursor()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS aruodas_uzsienis(
            id SERIAL primary key,
            flat_title VARCHAR(300),
            flat_price DECIMAL(10,2)
        )
    """

    cursor.execute(create_table_query)
    print("Table created Successfully!")


    url = "https://www.aruodas.lt/uzsienio-objektai/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    content_block = soup.select('div.project-list-item')



    for content in content_block:
        try:
            flat_title = content.find("h2", class_="project-title-full project-title").text.strip()
            flat_price = content.find("h3", class_="project-title-full project-min-values").text.strip() \
                .split(sep="Kaina:")[1].replace(" ", "").replace("€", "")
            # print(flat_title, flat_price)
            # flats_data.append((flat_title, flat_price))
            insert_query = "INSERT INTO aruodas_uzsienis (flat_title, flat_price) VALUES (%s, %s)"
            cursor.execute(insert_query, (flat_title, flat_price))

        except AttributeError:
            continue
    print("Flats inserted successfully!")


    connection.commit()

create_and_insert_flats()