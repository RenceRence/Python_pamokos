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


class svs:
    def __init__(self):
        self.studentu_sarasas=[]

    def prideti_studenta(self,studentas):
        self.vardas= input("Iveskite studento varda--->")
        self.pavarde=input("Iveskite studento pavarde--->")
        self.amzius=input("Iveskite amziu--->")
        self.studento_nr= input("Iveskite studento numeri--->")
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

