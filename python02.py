#Agatabrete 21.11.2023
#python harjutus 2
import turtle
import math

"""
Kilpkonn - küsib kasutajalt ringi raadiust
kasutab funktsiooni ringi joonistamiseks
"""
w = turtle.Screen()

def ring(r):
    john = turtle.Turtle()
    john.circle(r)
    
raadius = w.numinput("Ringi loomine","Sisesta ringi raadius:")

ring(raadius)
turtle.exitonclick()



"""
Rulluisutajad
Rulluisutaja keskmine kiirus on 29,9km/h
Kui kaugele jõuab 24minutiga
"""
kiirus = 29.9
aeg = 24
distants = round(kiirus / 60 * aeg, 2)
print("Kiirusega",kiirus, "km/h jõuab",distants,"km kaugusele")

"""
Leia kolmnurga hüpotenuus
Kolmnurga külgede pikkused on a=16 ja b=9
Kasuta Pythagorase teoreemi (a2 + b2 = c2) ja leia kolmnurga hüpotenuus
"""
a,b = 16, 9
c = round(math.sqrt(a**2 + b**2), 2)
print("Kolmnurga hüpoteenus on",c)

"""
Ajateisendus
Kasutaja sisestab aja minutites
Sinu valem leiab ja väljastab tunnid ja minutid
Näiteks: sisestus 72, vastus 1:12
"""
minutid = int(input("Sisesta aeg minutites:"))
h = minutid // 60
m = minutid % 60
print(h,":",m)

"""
Arvusüsteemid
Kasutaja sisestab täisarvu kümnendsüsteemis
Sinu programm teisendab selle 2nd ja 16nd süsteemi
"""
arv = int(input("Sisesta arv:"))
bii = bin(arv)
heks = hex(arv)
print(bii, heks)

"""
Kütusekulu arvutamine
Kasutaja sisestab tangitud kütuse liitrid
Kasutaja sisestab läbitud kilomeetrid
Programm leiab kütusekulu 100km kohta keskmiselt
"""
kytus = int(input("Sisesta liitrid:"))
km = int(input("Sisesta läbitud distants:"))
kytuse_kulu = kytus / (km / 100)
print(kytuse_kulu)



















