vaisiai=["Obuolys","Arbuzas","Bananas","Kriause","Citrina"]
ilgis=len(vaisiai)
print(ilgis)
print(vaisiai)
print(type(vaisiai))
print(vaisiai[2])
print(vaisiai[:2]) #rodys tik pirmus du is masyvo jei bus ::2 tai ims kas antra ims obuoli ir banana citrina,
o jei nuo galo tai pries skaiciu minusas -2
print(vaisiai[1:2]) #rodys ti antra, tai reiskia pirma ismeta
pridedame_vaisiu=vaisiai.append("Melionas")  #pridedame vaisiu su funkcija append
noriu prideti vaisiu tam tikroje vietoje insert(indeksas, vaisiaus pavadinimas)
vaisiai.insert(0,"Baklazanas")
keiciam_reiksme=vaisiai[0]="Kivis"# keiciame obuoli i kivi
print(vaisiai)
indeksas=vaisiai.index("Arbuzas")
print(indeksas)
vaisiai.remove("Bananas")
vaisiai.pop(2) # istrina pagal indeksa
print(vaisiai)
print(vaisiai[0])


dictionary-zodynas=my_dict={key1:value1,key2:value2,...}

zodynas={
    "Vardas":"Jonas",
    "Amzius":30,
    "Miestas":"Vilnius",
}
# print(zodynas["Amzius"])

# zodynas["ar_studentas"]=True
# del zodynas["Miestas"]    #norint istrinti
print(zodynas)

apsirasome didesni zodyna studentai galima labai daug prirasyti
studentai={
    "Jonas":{
        "Amzius":30,
        "Miestas":"Kaunas",
        "Profesija":"Inzinierius"
    },
    "Ona":{
        "Amzius":25,
        "Miestas":"Klaipeda",
        "Profesija":"Gydytoja"
    },
    "Maryte":{
        "Amzius":45,
        "Miestas":"Siauliai",
        "Profesija":"Mokytojas"
    },
    "Antanas":{
        "Amzius":70,
        "Miestas":"Kaunas",
        "Profesija":"Vairuotojas"
    },
}
print(studentai["Ona"])

studentai=[
    {
        "Vardas":"Jonas",
        "Amzius":30,
        "Miestas":"Kaunas",
        "Profesija":"Inzinierius"
    },
    {
        "Vardas":"Ona",
        "Amzius":25,
        "Miestas":"Klaipeda",
        "Profesija":"Gydytoja"
    },
    {
        "Vardas":"Maryte",
        "Amzius":45,
        "Miestas":"Siauliai",
        "Profesija":"Mokytojas"
    },
    {   "Vardas":"Antanas",
        "Amzius":70,
        "Miestas":"Kaunas",
        "Profesija":"Vairuotojas"
    },
]
naujas_studentas={                      #pridedane nauja studenta
    "Vardas":"Zose",
    "Amzius":20,
    "Miestas":"Vilnius",
    "Profesija":"Siuveja"
    }
studentai.append(naujas_studentas)
# print(studentai[1])
print(studentai)


prekiu_kategorijos=["Vaisiai","Mesa","Darzoves","Kepiniai"]

prekes={
    "Vaisiai":["Obuoliai","Bananai"],
    "Mesa":["Kiauliena", "Vistiena"],
    "Darzoves":["Bulves", "Pomidorai"],
    "Kepiniai":["Sausainiai","Tortai"]
}

#norime rasti prekes kategorija "Mesa"ir preke "Vistiena"

norima_kategorija="Mesa"
norima_preke="Vistiena"

if norima_kategorija in prekiu_kategorijos:
    if norima_preke in prekes[norima_kategorija]:
        print(f'parduotuveje yra {norima_preke}')
    else:
        print (f'Parduotuveje nera {norima_preke}')
else:
    print (f'parduotuveje nera prekiu kategorijos:{norima_kategorija}')
# print()
# # print(f'Mano parduotuves prekiu kategorijos {prekiu_kategorijos} is kuriu galite rinktis')   #f'' reiskia formatavima
# 1 dalis. Sukurkite sąrašą su žmonių vardais ir amžiumi:
zmones=[
    {"Vardas":"Jonas",
     "Amzius":42},
    {"Vardas":"Petras",
     "Amzius":18},
    {"Vardas":"Maryte",
     "Amzius":11},
    {"Vardas":"Zina",
     "Amzius":25},
    {"Vardas":"Kazys",
     "Amzius":50},
    {"Vardas":"Sarunas",
     "Amzius":12},
    {"Vardas":"Zose",
     "Amzius":35}
]
# print(zmones)

amzius=zmones [1]["Amzius"]
vardas=zmones[1]["Vardas"]

# 2 dalis. Jūsų užduotis - parašyti kodą, kuris išvestų kiekvieno žmogaus vardą su amžiumi: "nepilnametis",
# "suaugęs" arba "vaikas" (jei amžius yra 18).
if amzius>=18:
    print (f'Zmogus "{vardas}" suauges')
elif amzius<12:
    print (f'Zmogus "{vardas}" vaikas')
else:
    print (f'Zmogus "{vardas}" nepilnametis')

KITAS VARIANTAS
 1 dalis. Sukurkite sąrašą su žmonių vardais ir amžiumi:
zmones=[
    {"Vardas":"Jonas",
     "Amzius":42},
    {"Vardas":"Petras",
     "Amzius":18},
    {"Vardas":"Maryte",
     "Amzius":11},
    {"Vardas":"Zina",
     "Amzius":25},
    {"Vardas":"Kazys",
     "Amzius":50},
    {"Vardas":"Sarunas",
     "Amzius":12},
    {"Vardas":"Zose",
     "Amzius":35}
]
print(zmones)
zmogus=zmones[1]

# 2 dalis. Jūsų užduotis - parašyti kodą, kuris išvestų kiekvieno žmogaus vardą su amžiumi: "nepilnametis",
# "suaugęs" arba "vaikas" (jei amžius yra 18).
if zmogus["Amzius"]>18:
    print (f'"{zmogus}" suauges')
if zmogus["Amzius"]==18:
    print (f'"{zmogus}" Pauglys')
if zmogus["Amzius"]<18:
        print (f'"{zmogus}" nepilnametis')





1 dalis: Sukurkite žodyną su darbuotojo informacija(Vardas, atlyginimas,pareigos);
2.dalis: Pagal darbuotojo pareigas (jei jis yra "inžinierius"), padidinkite jo atlyginimą 10%. Jei jis nėra
"inžinierius", palikite atlyginimą nepakeistą.
darbuotoju_informacija=    {"Vardas":"Petras",
     "Atlyginimas": 2200,
     "Pareigos":"Inzinierius"
}

if darbuotoju_informacija ["Pareigos"]=="Inzinierius":
    # darbuotoju_informacija ["Atlyginimas"] = darbuotoju_informacija ["Atlyginimas"] * 1.10
    darbuotoju_informacija["Atlyginimas"]*=1.10
print (darbuotoju_informacija)

knygos=[
    {"pavadinimas":"Haris Poteris", "leidimo_metai":1997},
    {"pavadinimas":"Mobis Dikas", "leidimo_metai":1985},
    {"pavadinimas":"Deze", "leidimo_metai":2023},
    {"pavadinimas":"Puaro", "leidimo_metai":1970}
]
knyga=knygos[2]
knyga_pagal_ieskomus_metus=int(input("iveskite knygos isleidimo metus, kuriu ieskote >" ))
if knyga["leidimo_metai"]==knyga_pagal_ieskomus_metus:
    print (f"Ieskomos knygos pavadinimas {knyga['pavadinimas']}   metais yra: {knyga_pagal_ieskomus_metus} ")
if knyga["leidimo_metai"]!=knyga_pagal_ieskomus_metus:
    print(f"Ieskomos knygos pavadinimas nerasta ")
importuojamos bibliotekos VISADA rasomos pirmose eilutese
import os
# dabartinis_katalogas = os.getcwd()
#
#
# # norimas_aplankas = input("Iveskite aplanko pavadinima, kurio turini norte matyti ->  ")
#
# naujas_katalogas=input("Prasome nurodyt katalogo lokacija->")
# # keiciam_kataloga=os.chdir(naujas_katalogas)
# try:
#     keiciam_kataloga = os.chdir (naujas_katalogas)
#     if os.getcwd()==naujas_katalogas:
#         print(f"Darbinis katalogas sekmingai pakeistas i {naujas_katalogas}")
#     #bandome gautiaplanko turini;
#     turinys=os.listdir(naujas_katalogas)
#     print(",".join(turinys))
# except FileNotFoundError:
#     print(f"Deja aplankas' {naujas_katalogas}'nerastas")
import shutil
EXTENSION_MAP={
    '.jpg':"Images",
    '.jpeg':"Images",
    '.phg':"Images",
    '.gif':"Images",
    '.pdf':"Documents",
    '.txt':"Documents",
    '.doc':"Documents"
}

filename= input("Please the name of the file you want to organizer ->")

file_extension=os.path.splitext(filename)[1]

try:
    if os.path.exists(filename) and file_extension in EXTENSION_MAP:
        directory_name=EXTENSION_MAP[file_extension]

        #sukusrs kataloga jei jo nera
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)

            #perkelia faila
        shutil.move(filename, os.path.join(directory_name,filename))
        print(f"{filename} has been moved to {directory_name}")
    else:
        print("tokio failo nera arba jis neatpazintas")
except FileNotFoundError:
    print(f"Error: {filename} was not found")
except PermissionError:
    print(f"Error: You dont't have permissions to move '{filename}'")
Namų darbai:
1. Sukurkite prekių sąrašą su kainomis ir raskite brangiausią prekę.

prekes={
    "Sasiuvinys":1.20,
    "Tusinukas":13.50,
    "Trintukas":0.43,
    "Uzrasine":8.99
    }

brangiausia_preke=max(prekes,key=prekes.get)
brangiausia_kaina=prekes[brangiausia_preke]

print(f'Brangiausia preke yra {brangiausia_preke} ir kainuoja {brangiausia_kaina} euru.')

2. Sukurkite žodyną su studento pažymiais ir raskite ar studentas
išlaikė egzaminą;
studentas={
    "Matematika":8,
    "IT":7,
    "Anglu_kalba":4,
    "Filosofija":10
}
islaike=all(pazimys>=4 for pazimys in studentas.values())
if islaike:
    print("Studentas išlaikė egzaminą.")
else:
    print("Studentas neišlaikė egzamino.")


3. Sukurkite žodyną su kliento informacija ir patikrinkite ar jo sąskaitoje
yra pakankamai lėšų tam tikram pirkiniui.
klientas = {
    'vardas': 'Jonas',
    'saskaita': 'LT123456789',
    'likutis': 110.0
}

pirkinio_kaina = 300.0

if klientas['likutis'] >= pirkinio_kaina:
    print(f"{klientas['vardas']} gali atlikti pirkinį už {pirkinio_kaina} eurų.")
else:
    print(f"{klientas['vardas']} neturi pakankamai lėšų pirkinio atlikimui.")


4.Pagal nurodytą pajamų sumą, paskaičiuokite mokesčius, taikant šias taisykles:
pajamoms iki 1000 - 10%, nuo 1001 iki 5000 - 15%, virš 5000 - 20%.

pajamos=6000
if pajamos<1000:
    mokestis=pajamos*0.10
if pajamos<=5000:
    mokestis=pajamos*0.15
if pajamos>5000:
    mokestis=pajamos*0.20

print(f'pajamos  {pajamos}')
print (f'mokestis {mokestis}')

-------------rosvaldo
pajamos = -25

if pajamos > 5000:
    print("Mokesciu suma", + pajamos * 0.2)
elif pajamos > 1000:
    print("Mokesciu suma", + pajamos * 0.15)
elif pajamos > 0:
    print("Mokesciu suma", + pajamos * 0.1)
else:
    print("Pajamu nera")