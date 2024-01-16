#Agatabrete
#21.11.23
#Harjutus 4
import random
"""
Ruutude ja kuupide tabel
Programm leiab ja väljastama ruudud ja kuubid arvudele 1..10.
Vorminda tabel tulpades.
Arv Ruut Kuup
1   1    1
2   4    8
3   9    27
4   16   64
jne
"""
print(f"Arv Ruut Kuup")
for i in range(1,11):
    print(f"{i} {i**2:5} {i**3:5}")
    

input()
"""
Pank
Kasutaja soovib panka panna raha teatud aastateks.
Panga intress on 5% summast. Leia kui palju ta summa iga aasta kasvab.
Vorminda tabel tulpades.
Näiteks: paneme panka 10000€ ja 5 aastaks
Aasta   Algsumma    Intress     Aasta lõpuks
1       10000.00    500.00      10500.00
2       10500.00    525.00      11025.00
3       11025.00    551.25      11576.25
4       11576.25    578.81      12155.06
5       12155.06    607.75      12762.82
Summa kokku: 12762.82€
Kasum: 2762.82€
"""
raha = 10000
aasta = 5
konto = raha
intress = 0.05

print("Aasta   Algsumma    Intress     Aasta lõpuks")
for i in range(aasta):
    print(f"{i+1} {konto:>14.2f} {konto*intress:>9.2f} {konto + konto * intress:>13.2f}")
    konto = konto + konto * intress

print(f"Summa kokku: {konto:.2f}€")
print(f"Kasum: {konto-raha:.2f}€")
input()



"""
Arvamismäng
Kasutaja saab arvata arvuti poolt loodud arvu 3 korda.
Õnnitle kasutajat, kui arvas selle ära.
Kui mitte, siis küsi, kas ta soovib veel arvata.
"""
loop = 1
voidud = 0


while loop == 1:
    print("----------- ARVAMISMÄNG -----------")
    suv = random.randint(1,10)
    #print(suv)
    for i in range(3):
        arva = int(input("Paku arv 1-10: "))
        if suv == arva:
            print("Arvasid ära!")
            voidud = voidud+1
            break
        else:
            print("Proovi veel!")
    print("------------ GAME OVER -------------")
    print(f"Võidud: {voidud}")
    jatka = input("Soovid jätkata? y/n: ")
    if jatka == "n":
        loop = 0
     
    
    
input()
"""
Viisikud
Programm väljastab ainult 5ga jaguvad arvud 1-100
"""
for i in range(1,101):
    if i%5 == 0:
        print(i)

"""
Pisike korrutustabel
Koosta programm, mis tekitab automaatselt viiega korrutustabeli.
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
"""
for j in range(1,11):
    for i in range(1,11):
        print(f" {j} x {i} = {j*1}")


"""
Paaris ja paaritu
Loo tsükkel, mis genereerib arvud 1-100 koos vastava tekstiga, kas arv on paaris või paaritu
"""
for i in range(1,11):
    if i % 2 == 0:
        v = "paaris"
    else:
        v = "paaritu"
    print(i,v)


"""
Loto
Koosta tsükli abil programm, mis kuvab 5 suvalist  ühekohalist numbrit. Näiteks 53542
"""
import random

for i in range(5):
    print(random.randint(0,9),end="")

print()
"""
Tärnid
Loo tsükkel, mis väljastab 5×5 tärnid
Loo tsükkel, mis väljastab tärnidest kasvava kolmnurga
Loo tsükkel, mis väljastab tärnidest kahaneva kolmnurga
"""

arv = 5
for i in range(5):
    print("* "*arv)
    arv = arv - 1
print()
arv = 5
for i in range(arv):
    print("* "*(i+1))
print()
arv = 5
for i in range(arv):
    print("* "*arv)

"""
Jalgpalli meeskond
Sa pead looma programmi, mis kontrollib kas kandideerija sobib antud meeskonda.
Vanus peab jääma vahemikku 16-18 ning lubatud on ainult meessugu.
Täienda programmi nii, et kui kandideerija on naissoost, siis vanust üldse ei küsita.
"""
sugu = "mees"
if sugu == "mees":
    vanus = 11
    if vanus >= 16 and vanus <= 18:
        print("Tere tulemast meeskonda!")
    else:
        print("Vanus ei sobi")
else:
    print("Ei pääse meeskonda")




"""
Müük
Kasutaja sisestab toote hinna. Kui see on hinnaga kuni 10€, saab ta allahindlust 10%. Üle 10€ tooted saavad soodukat 20%.
Kuva toote lõplik hind. Plokkskeemi pole vaja!
"""
hind = 10
if hind <= 10:
    ale = 0,1    
else:
    ale = 0,2
    
#print(f"Sinu soodushind on {vastus}", hind - (hind * ale))

    
"""
Juubel
Kasutaja sisestab oma sünnipäeva ja sinu programm ütleb, kas tegemist on juubeliga.
Plokkskeemi pole vaja!
"""
v = 10
if v % 5 == 0:
    vastus = "on"
else:
    vastus = "ei ole"
print(f"Vanus {v}: {vastus}juubel")

"""
Matemaatika
Kasutaja sisestab kaks arvu ning programm küsib kasutajalt, mis tehet ta soovib (+-*/) ning viib kasutaja valiku ellu.
Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.
"""
nr1 = int(input("arv1: "))        
nr2 = int(input("arv2: "))
tehe = input("Vali tehe + - * /: ")

if tehe == "+":
    vastus = nr1 + nr2
elif tehe == "-":
    vastus = nr1 - nr2
elif tehe == "*":
    vastus = nr1 * nr2
elif tehe == "/":
    vastus = round(nr1 / nr2, 2)
else:
    vastus = "ära pulli mees"
    
print(f"{nr1} {tehe} {nr2} = {vastus}") 
    
    
"""
Ruut
Kasutaja sisestab ruudu küljed ning programm tuvastab kas tegemist saab olla ruuduga.
Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.
"""
nr1 = int(input("Ruudu 1. külg: "))        
nr2 = int(input("Ruudu 2. külg: "))

if nr1 == nr2:
    print("ruut")
else:
    print("pole ruut")