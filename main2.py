# objektinis programavimas.
# Visi objektai aprasomi klasemis
# # klase

# class automobilis:
#     def __init__(self, marke, modelis, metai):
#         self.marke =marke
#         self.modelis =modelis
#         self.metai =metai
# # metodas

#     def automobilio_pavadinimas(self):
#         return f" Automobilis: {self.marke}\n , automobilio modelis: {self.modelis}\n , metai {self.metai}\n"
#
# #objektas

# auto1 = automobilis("Audi","A8",2021)
# print(auto1.automobilio_pavadinimas())
#
# --------------------------------------------------------------------------------------------------------------
#
# class automobilis:
#     def __init__(self, marke, modelis, metai, variklio_turis, kuro_tipas):
#         self.marke =marke
#         self.modelis =modelis
#         self.metai =metai
#         self.variklio_turis=variklio_turis
#         self.kuro_tipas = kuro_tipas
#         self.rida = 0
#
# # metodas
#
#     def automobilio_pavadinimas(self):
#         return f" Automobilis: {self.marke}\n , automobilio modelis: {self.modelis}\n , metai {self.metai}\n"
#
#     def vaziuoti (self,km):
#         self.rida += km
#         return f"vaziuojama {km} km.Bendra rida {self.rida} km"
#
# #objektas
#
# auto1 = automobilis("Audi","A8",2021,3.0,"Benzinas")
# print(auto1.automobilio_pavadinimas())
# print (auto1.vaziuoti(150))
# -------------------------------------------------------------------------------------
#
# class gyvunas(object):
#     def __init__(self, rusis, svoris, amzius, vardas):
#         self.rusis = rusis
#         self.svoris = svoris
#         self.amzius = amzius
#         self.vardas = vardas
#
#     def gyvuno_pavadinimas(self):
#         return f"Gyvuno rusis: {self.rusis}\n gyvuno svoris: {self.svoris}\n amzius {self.amzius}\n vardas {self.vardas}"
#
#     def valgyti(self):
#         return f"{self.vardas} valgo"
#
#     def prisistatymas(self):
#         return f" Mano vardas {self.vardas}, esu {self.rusis} "
#
#
# lape = gyvunas("ryza", 25, 3, "Zose")
# kate = gyvunas("kaimiskas", 6, 7, "Pukis")
# # print(lape.gyvuno_pavadinimas())
# # print(lape.valgyti())
# print(lape.prisistatymas())
# print()
# print(kate.prisistatymas())
# # print(kate.gyvuno_pavadinimas())
# # print(kate.valgyti())
#----------------------------------------------------------------------------------------
# darbotverkes sudarymas
#
# from colorama import init, Fore
# init()
# class Uzduotis:
#
#     def __init__(self, pavadinimas, aprasymas):
#         self.pavadinimas=pavadinimas
#         self.aprasymas=aprasymas
#         self.atlikta=False
#
#     def atlikimas(self):
#         self.atlikimas=True
#         print (f"{Fore.LIGHTGREEN_EX}Uzduotis {self.pavadinimas} buvo atlikta ")
#
#     def info(self):
#         return f"{Fore.BLUE}Pavadinimas {self.pavadinimas}\n  Aprasymas: {self.aprasymas}\n  "
#
#
# class ToDo_sarasas:
#     def __init__(self):
#         self.uzduociu_sarasas=[]
#
#     def prideti_uzduoti(self, pavadinimas, aprasymas):
#         uzduotis = Uzduotis(pavadinimas,aprasymas)
#         self.uzduociu_sarasas.append(uzduotis)
#
#     def visos_uzduotys(self):
#         if not self.uzduociu_sarasas:
#             print(f"{Fore.RED}Uzduociu sarasas yra tuscias")
#         for uzduotis in self.uzduociu_sarasas:
#             print(uzduotis.info())
#
#     def pazymeti_kaip_atlikta(self,pavadinimas):
#         for uzduotis in self.uzduociu_sarasas:
#             if uzduotis.pavadinimas==pavadinimas:
#                 uzduotis.atlikimas()
#                 return
#         print (f' {Fore.RED} uzduotis pavadinimu: {pavadinimas} nerasta')
#
#
# ToDo_sarasas=ToDo_sarasas()
# while True:
#     print("\n Pasirinkite veiksma:")
#     print("1. prideti uzduoti")
#     print("2. Perziureti uzduoti")
#     print("3. Pazymeti uzduoti kaip atlikta")
#     print ("4. Iseiti")
#
#     pasirinkimas= input()
#     if pasirinkimas=="1":
#         pavadinimas= input("Iveskite uzduoties pavadinima---->")
#         aprasymas=input("Iveskite uzduoties aprasyma---->")
#         ToDo_sarasas.prideti_uzduoti(pavadinimas,aprasymas)
#         print(f"{Fore.MAGENTA} Uzduotis sekmingai prideta")
#     elif pasirinkimas=="2":
#         ToDo_sarasas.visos_uzduotys()
#     elif pasirinkimas=="3":
#         pavadinimas= input(f"{Fore.} Iveskite uzduoties pavadinima kuria norite pakeisti --->")
#         ToDo_sarasas.pazymeti_kaip_atlikta(pavadinimas)
#     elif pasirinkimas=="4":
#         print("Iseinama....")
#         break
#     else:
#         print("neteisingas pasirinkimas prasome bandyti dar karta ")
#
# banko saskaita is kurios galima ideti ir isimti pinigus
#
# class bankas:
#     def __init__(self, vardas, pavarde,likutis=0):
#         self.vardas=vardas
#         self.pavarde=pavarde
#         self.likutis=likutis
#
#     def inesti(self, suma):
#         if suma>=10:
#             self.likutis+=suma
#             print (f"Pinigu suma {suma} sekmingai prideta prie saskaitos {self.likutis}")
#         else:
#             print(f"Klaida!!!! Inesama suma per maza")
#
#     def isimti(self,suma):
#         if suma>0:
#             if suma<=self.likutis:
#                 self.likutis-=suma
#                 print (f"Pinigu suma sekmingai nuimta {suma}")
#         else:
#             print(f"Suma per didele, nepakankamas likutis ")
#     def pz_likutis(self):
#         return f"{self.vardas},{self.pavarde} saskaitoje turi {self.likutis}"
#
# saskaita1=bankas("Petras","Petraitis",25)
# print()
# saskaita1.inesti(1000)
# print()
# saskaita1.isimti(500)
# print()
# print(saskaita1.pz_likutis())
# print()
# #---------------------------------------------------------------------------------------------------------

#Sukurkite Studentas klase kuri reprezentuoja individualų studentą, turintį savo vardą, pavardę, amžių,
# studento numerį ir pažymių sąrašą. Antroje klasėje StudentuValdymoSistema - tai klasė, skirta valdyti
# studentų sąrašą. Ji leidžia pridėti naujus studentus, gauti informaciją apie konkretų studentą pagal jo
# numerį ir išvesti visų studentų informaciją.
# Sukurkite metoda kuris isves studento vidurki;
# sukurkite metoda kad galetumete prideti studenta;
# Sukurkite metoda kuris grazins visa studento info;
#Sukurkite metoda kuris pasalintu studenta;

class Studentas:
    def __init__(self,vardas, pavarde, amzius, studento_nr, pazymiai=None):
        self.vardas=vardas
        self.pavarde=pavarde
        self.amzius=amzius
        self.studento_nr=studento_nr
        self.pazymiai=pazymiai if pazymiai else []

    def studento_vidurkis(self):
        return sum(self.pazymiai)/len(self.pazymiai) if self.pazymiai else 0

    def prideti_pazymi(self,pazymys):
        self.pazymiai.append(pazymys)

    def info(self):
        return (f"Studentas {self.vardas} {self.pavarde}, kurio amzius {self.amzius}. Studento numeris"
                f" {self.studento_nr} Pazymiai {self.pazymiai}  ")

    def pasalinti_pazym(self,pazymys):
        if 0<=pazymys < len(self.pazymiai):
            del self.pazymiai[pazymys]
        else:
            print(f"Pazymis nerastas")

    def __str__(self):
        return f"{self.vardas} {self.pavarde} {self.amzius} {self.studento_nr} {self.pazymiai}"


class svs:
    def __init__(self):
        self.studentu_sarasas=[]

    def prideti_studenta(self, studentas):
        self.studentu_sarasas.append(studentas)
        print(f"Studentas sekmingai pridetas")

    def pasalinti_studenta(self,studento_nr):
        naujas_studentu_sarasas=[]
        for s in self.studentu_sarasas:
            if s.studento_nr !=studento_nr:
                naujas_studentu_sarasas.append(s)
        self.studentu_sarasas=naujas_studentu_sarasas

    def visi_studentai(self):
        return self.studentu_sarasas

    def __str__(self):
        return "\n ".join (str(studentas) for studentas in self.studentu_sarasas)


studentu_sistema =svs()
studentas1=Studentas("Petras","Petraitis",25, 1)
studentas2=Studentas("Jonas", "Jonaitis",30,3)
studentas1.prideti_pazymi(5)
studentas1.prideti_pazymi(8)
studentas1.prideti_pazymi(10)
studentas2.prideti_pazymi(7)
studentas2.prideti_pazymi(4)
# svs.visi_studentai()
# studentas1.pasalinti_pazym(2)
# print(studentas1.info())
# print(studentas2.info())
# studentas1.pasalinti_pazym(0)
# # studentu_valdymo_sistema.pasalinti_studenta()
# print(studentas2.info())
# print(studentas1.info())
#
# svs.visi_studentai(studentas2)
# # studentu_valdymo_sistema.pasalinti_studenta(3)
for studentas in svs.visi_studentai():
    print(studentas)
