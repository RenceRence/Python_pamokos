import requests
from bs4 import BeautifulSoup

import psycopg2

flat_date=[]
def creat_and_insert_flats():
    connection=psycopg2.connect(
        host="localhost",
        port=5432,
        database="Aruodas",
        user="postgres",
        password="23duomenubaze23"
    )
    cursor=connection.cursor()

    create_table_query="""
    CREATE TABLE IF NOT EXISTS Uzsienio_top(
        id SERIAL primary key,
        flat_title VARCHAR(1000),
        flat_price DECIMAL(10,2)
    )"""

    cursor.execute(create_table_query)
    print ("Table create Successfully")

    url="https://www.aruodas.lt/uzsienio-objektai/"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"html.parser")

    content_block=soup.select('div.project-list-content div')
    for content in content_block:
        try:
            flat_title=content.find("h2", class_="project-title-full project-title").text.strip()
            flat_price=content.find("h3", class_="project-title-full project-min-values").text.strip() \
                .replace(" ", "").replace("€","").split(sep="Kaina:")[1]
            cursor.execute("select 1 from uzsienio_top where flat_title=%s and flat_price=%s",(flat_title,float(flat_price)))
            exists=cursor.fetchone()
            if not exists:
                cursor.execute( "INSERT INTO uzsienio_top (flat_title, flat_price) VALUES (%s, %s)", (flat_title,float(flat_price)))
            # print(flat_title,flat_price)
            # flat_date.append((flat_title,flat_price))
            # if select_query="SELECT * FROM uzsienio_top(flat_title,flat_price)" !=uzsienio_top:
            #     insert_query = "INSERT INTO uzsienio_top (flat_title, flat_price) VALUES (%s, %s)"
            #     cursor.execute(insert_query, (flat_title, flat_price))

        except AttributeError:
            continue

    connection.commit()
creat_and_insert_flats()


