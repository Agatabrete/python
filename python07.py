#funktsioonid
#5.12.23
#Agata Brete
"""
1.Koosta funktsioon,
mille väljakutsumisel tevitab kasutajat tema enda nimega
2.Täienda eelmist funktsiooni nii, mis tervitab mind eesti või inglise keeles.
Vaikimisi tervitatakse mind hoopis saksa keeles.
3.Koosta ruumalade leidmise programm. Kasutajalt küsitakse,
millise kujundi ruumala on vaja leida ja siis vajalikke argumente. Kasutada tuleb funktsioone. Tore,
kui programm ei lõpetaks kohe töö vaid lubab valida teisi ruumalasid
"""
def tervita(nimi, keel="de"):
    if keel == "en":
        print(f"Hi {nimi}!")
    elif keel == "et":
        print(f"Tere {nimi}!")
    else:
        print(f"Hallo {nimi}!")

tervita("Agata")

def kuup(a,b,c):
    v = a*b*c
    print(f"Kuubi ruumala on: {v} ")

def kera(r):
    v = round(4*math.pi*r**2,2)
    print(f"Kera ruumala on : {v} ")

def koonus():
    print("koonus")

def silinder():
    print("silinder")

loop = 1
print("-------------\nLEIAME RUUMALA\n-----------")
while loop==1:
    print("Vali Kujund:\n1. Vali kuup \n2. Vali kera \n3. koonus \n4. silinder \n5. EXIT\n--------------- ")
    valik = int(input("Tee Valik: "))

    if valik == 1:
        a = int(input("Külg 1: "))
        b = int(input("Külg 2: "))
        c = int(input("Külg 3: "))
        kuup(a,b,c)
    elif valik == 2:
        r = int(inpt("Sisesta raadius: "))
        kera(r)
    elif valik == 3:
        print(koonus())
    elif valik == 4:
        print(silinder())
    else:
        loop = 0
    print("\n-------------\n")

