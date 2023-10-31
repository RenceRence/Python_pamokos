class Studentas:
    def __init__(self, vardas, pavarde, amzius, studento_numeris, pazymiai=None):
        self.vardas = vardas
        self.pavarde = pavarde
        self.amzius = amzius
        self.studento_numeris = studento_numeris
        self.pazymiai = pazymiai if pazymiai else []

    def studento_vidurkis(self):
        return sum(self.pazymiai) / len(self.pazymiai) if self.pazymiai else 0

    def prideti_pazymi(self, pazymys):
        self.pazymiai.append(pazymys)

    def studento_informacija(self):
        return (f'Studento vardas {self.vardas}, studento pavarde {self.pavarde}, amzius {self.amzius}, '
                f'studento numeris {self.studento_numeris}, pazymiai {self.pazymiai}')

    def pasalinti_pazymi(self,pazymys):
        if 0 <= pazymys < len(self.pazymiai):
            del self.pazymiai[pazymys]
        else:
            print("Toks pazymys nerastas")

class StudentuValdymoSistema:
    def __init__(self):
        self.studentu_sarasas = []

    def prideti_studenta(self, studentas):
        self.studentu_sarasas.append(studentas)
        print("Studentas sekmingai pridetas")

    def pasalinti_studenta(self,studento_numeris):
        naujas_studentu_sarasas = []
        for s in self.studentu_sarasas:
            if s.studento_numeris != studento_numeris:
                naujas_studentu_sarasas.append(s)
        self.studentu_sarasas = naujas_studentu_sarasas

    def visi_studentai(self):
        return self.studentu_sarasas

    def __str__(self):
        return "\n ".join(str(studentas) for studentas in self.studentu_sarasas)

studentu_sistema = StudentuValdymoSistema()
studentas1 = Studentas("Jonas", "Jonaitis", 23, 102)
studentas2 = Studentas("Petras", "Petraitis", 21, 105)
studentas1.prideti_pazymi(7)
studentas1.prideti_pazymi(3)
studentas1.prideti_pazymi(5)
studentas2.prideti_pazymi(8)
studentas2.prideti_pazymi(6)
# print(studentas1.studento_informacija())
# studentas1.pasalinti_pazymi(0)
# print(studentas1.studento_informacija())
# print(studentas2.studento_informacija())
# studentu_sistema.pasalinti_studenta(105)
# print(studentas2.studento_informacija())
for studentas in studentu_sistema.visi_studentai():
    print(studentas)



    # margaritos variantas