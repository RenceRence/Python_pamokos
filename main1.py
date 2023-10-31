for ciklas jis kartoja tam tikrus veiksmus, tol kol jis turi ka testuoti
for raktas in seka:
print(raktas)
for i in range(5):
    print(i)

sarasas=[1,2,3,4,5]
for skaicius in sarasas:
    print(skaicius)

tekstas="Python data science"

for raide in tekstas:
    print(raide)

zodynas={"a":1,"b":2,"c":3,"d":4}
for raktas in zodynas:
    print(raktas,zodynas[raktas])

sarasas=[1,2,3,4,5]
for skaicius in sarasas:
    if skaicius==3:
        continue #break
    print(skaicius)

skaiciai=[10,20,30,40,50]   #ismes visus skaicius kurie yra didesni uz vidurki. vidurkis gaunasi 30, o atsakyma atiduos 40 ir 50

suma=sum(skaiciai)
vidurkis=suma/len(skaiciai)

for skaicius in skaiciai:
    if skaicius>vidurkis:
        print(skaicius)


sarasas=["jonas","antanas","ona","marija" ]
print('\n'.join(sarasas))

for vardas in sarasas:
    print(vardas +'\n')

tekstas="Python data science"

for raide in reversed(tekstas):
    print(raide)


tekstas="Python"
tuscias=""
for raide in tekstas:
    tuscias=raide+tuscias
    print (tuscias)


visa daugybos lentele
max_skaicius=10

for i in range(1,max_skaicius+1):
    for j in range(1,max_skaicius+1):
        print (i*j, end="\t")  #\t reiskia tarpai
    print ()

pasirasytti lista kuriame butu tekstas ir zodziai iskirtas i skirtingus indeksus

tekstas=["Labas","rytas", "cia", "ir", "as"]
sakinys=""
for zodis in tekstas:
    sakinys+=zodis+" "
sujungtas_tekstas=sakinys.rstrip()
print (sujungtas_tekstas)


sarasas = ["labas", "rytas", "suraitytas", "skanios", "kavytes"]
for i in sarasas:
    print(i, end=" ")


while

skaicius=19
while skaicius<=20:
    print(skaicius)
    skaicius+=1

ivestis=int(input("Iveskite teigiama skaiciu:->"))

while ivestis<0:
    print("Jusus skaicius neiiamas")
    ivestis=int(input("Bandykite dar karta "))
print("ivedete teigiama skaiciu" ,ivestis)

spejimas= int(input("Spekite skaiciu nuo 1 iki 10 ---->"))
atsakymas=5

while spejimas!= atsakymas:
    spejimas=int(input("Atsakymas neteisingas. Bandykite dar karta ------>"))
print("Sveikinam jus atspejot")

while True:
    print("-------Meniu-------")
    print("1. Atspausdinti pasveikinima")
    print("2. Iveskite nauja varda")
    print ("3. iseiti")
    pasirinkimas=input("Iveskite savo pasirinkima (1/2/3)--->")
    if pasirinkimas=="1":
        print (f"labas")
    elif pasirinkimas=="2":
        vardas=input("Iveskite nauja varda--->")

        print ("Sekmingai ivedete nauja varda")
        print(f"Jusu vardas pakeistas i {vardas}")
    elif pasirinkimas=="3":
        print ("Aciu, kad naudojates programas.IKI")
        break
    else:
        print ("Neteisingas pasirinkimas. Bandykite dar karta")

parasyti programa kuri atspetu paslaptinga zodi jei netepeja speja is naujo kol neatspes

zodis= "kepure"
spejamas_zodis=input("Iveskite spejama zodi---->")

while spejamas_zodis!=zodis:
    spejamas_zodis=(input("Bandykite dar karta "))
print("jusu zodis neteisingas")

program, kurioj irasius skaicius ir man turi ismesti to skaiciaus daugybos lentele , pvz 5*1=5, 5*2=10...

skaicius=1
skaicius2=int(input("Iveskite daugikli--->"))

while skaicius<=5:
    sandauga=skaicius*skaicius2

    print(f"Dauginame {skaicius}*{skaicius2}={sandauga}")
    skaicius+=1

    pasirinkimas = int(input("Pasirinkite skaiciu nuo 1 iki 10: "))
max_skaicius = 1
while max_skaicius <= 10:
    rezultatas = max_skaicius*pasirinkimas
    print(f'{pasirinkimas} * {max_skaicius} = {rezultatas}')
    max_skaicius += 1

pasirenkamas_skaicius = int(input("pasirinkite skiaciu nuo 1 iki 10->"))

x = range(1,11)
for i in x:
    rezultatas = pasirenkamas_skaicius * i
    print(i, "x", pasirenkamas_skaicius, "=", rezultatas)


FUNKCIJOS

def pasisveikinimas():
    print("Labas")

if __name__=='__main__': #niekada nesikeis
    pasisveikinimas()

def hello():
    print("Hello")

hello()


def hello(vardas):
    print(f"Hello {vardas}")
hello("Renata")


def suma(a,b):
    return a+b
atsakymas=suma(5,3)
print(atsakymas)

susikursime knygu valdymo sistema kur mes galetume prideti perziureti ar isrinkti knygas

def rodyti_meniu():
    print("-----Meniu-----")
    print("1. Prideti knyga")
    print("2. Perziureti visas knygas")
    print("3. Ieskoti knygos pagal pavadinima")
    print("4. Iseiti")

rodyti_meniu()     #funkcijos iskvietimas

def rodyti_meniu():
    print("-----Meniu-----")
    print("1. Prideti knyga")
    print("2. Perziureti visas knygas")
    print("3. Ieskoti knygos pagal pavadinima")
    print("4. Iseiti")

def prideti_knyga(knygu_sarasas):
    pavadinimas= input("Iveskite knygos pavadinima--->")
    autorius=input("Iveskite knygos autoriu--->")
    knygu_sarasas.append({"pavadinimas":pavadinimas, "autorius":autorius})
    print(f"Knyga'{pavadinimas}'prideta!")

def perziureti_knygas(knygu_sarasas):
    for knyga in knygu_sarasas:
        print(f"Pavadinimas:{knyga['pavadinimas']}, Autorius:{knyga['autorius']}")

def ieskoti_knygos(knygu_sarasas):
    ieskoma_knyga=input("Iveskite knygos pavadinima kurios ieskote--->")
    rasti_knygas=[knyga for knyga in knygu_sarasas if ieskoma_knyga.lower() in knyga['pavadinimas'].lower()]
    if rasti_knygas:
        for knyga in rasti_knygas:
            print(f"Pavadinimas:{knyga['pavadinimas']}, Autorius: {knyga['autorius']}")
    else:
        print(f"Knyga su paadinimu:'{ieskoma_knyga}' nerasta")

def main():
    knygu_sarasas=[]

    while True:
        rodyti_meniu()
        pasirinkimas=input("Pasirinkite veiksma(1-4)--->")
        if pasirinkimas=="1":
            prideti_knyga(knygu_sarasas)
        elif pasirinkimas=="2":
            perziureti_knygas(knygu_sarasas)
        elif pasirinkimas=="3":
            ieskoti_knygos(knygu_sarasas)
        elif pasirinkimas=="4":
            print("Viso!!!!")
            break
        else:
            print("Neteisingas pasirinkimas. Prasome pasirinkti nuo 1 iki 4")


main()

bankine sistema, mes turime ideti pinigus isimt pinigus, perziureti balansa , atidaryti saskaita, uzdaryti saskaita ir pan.

saskaitos={


}
def rodyti_meniu():
    print("-----Mini banko sistema-----")
    print("1. atidaryti nauja saskaita")
    print("2. Inesti pinigus")
    print("3. Nusiimti pinigus")
    print("4. Perziureti saskaitos likuti")
    print("5. Uzdaryti sakaita")
    print("6. Iseiti")

def atidaryti():
    vardas= input("Iveskite savo varda--->")
    likutis=int(input ("Iveskite pinigu likuti--->"))
    saskaitos_nr=len(saskaitos)+1
    saskaitos[saskaitos_nr]={"vardas":vardas, "likutis":likutis}
    print(f"Saskaita '{vardas}'   atidaryta su likuciu '{likutis}'")

def inesti():
    saskaitos_nr=int(input("Iveskite saskaitos numeri--->"))
    inesama_suma=float(input(f"Iveskite suma kuria norite inesti--->"))
    saskaitos[saskaitos_nr]["likutis"]+=inesama_suma
    print (f"I saskaita '{saskaitos_nr}' sekmingai inesta '{inesama_suma}'")

def issiimti():
    saskaitos_nr=int(input("Iveskite saskaitos numeri--->"))
    nuimama_suma=int(input(f"Iveskite suma kuria norite nusiimti-->"))
    if nuimama_suma<=saskaitos[saskaitos_nr]["likutis"]:
        saskaitos[saskaitos_nr]["likutis"]-=nuimama_suma
        print (f"I saskaita '{saskaitos_nr}' sekmingai inesta '{nuimama_suma}'")
    else:
        print (f"Saskaitoje '{saskaitos_nr}' nepakanka pinigu")

def perziureti():
    saskaitos_nr= int(input("Iveskite sakaitos numeri--->"))
    likutis2=saskaitos[saskaitos_nr]["likutis"]
    print (f"saskaitos nr '{saskaitos_nr}' likutis yra '{likutis2}' eurais")

def uzdaryt():
    saskaitos_nr= int(input("Iveskite sakaitos numeri--->"))
    del saskaitos[saskaitos_nr]
    print(f"Saskaitas, su saskaitos nr '{saskaitos_nr}' sekmingai i6trinta")

def main():
    saskaitos=[]
    while True:
        rodyti_meniu()
        pasirinkimas=input("Pasirinkite veiksma(1-6)--->")
        if pasirinkimas=="1":
            atidaryti()
        elif pasirinkimas=="2":
            inesti()
        elif pasirinkimas=="3":
            issiimti()
        elif pasirinkimas=="4":
            perziureti()
        elif pasirinkimas=="5":
            uzdaryt()
        elif pasirinkimas=="6":
            print("Viso gero!!!!")
            break
        else:
            print("Neteisingas pasirinkimas. Prasome pasirinkti nuo 1 iki 6")

main()

Sukurkite funkciją pvm_skaiciuokle(), kuri priimtų kainą be PVM ir grąžintų kainą su 21% PVM.

def pvm_skaiciuokle(kaina):
    pkaina=kaina+kaina*pvm/100
    print(f"kainos {kaina} su PVM lygi {pkaina}")

kaina =float(input(f"Iveskite kaina kurios PVM skaiciuosim--->"))
pvm=int(input("Iveskite PVM dydi--->"))
pvm_skaiciuokle(kaina)
-------------------------------------------------------------------rosvaldo
def be_pvm(kaina):
    return kaina * 1.21

kaina_su_pvm = be_pvm(int(input("Iveskite kaina be PVM: ")))
print("Kaina su PVM", + kaina_su_pvm)