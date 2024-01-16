#tekstifailid
#5.12.23
#Agata Brete

"""
Sinu ülesanne on koostada programm, mis kuvab pooliitikud inimsilmale sõbralikus vaates.
Andra      Veidemann  SDE        3469      
Evelyn     Sepp       KE         3569      
Juku-Kalle Raid       IRL        4275      
Jörgen     Siil       SDE        1865      
Keit       Pentus     RE         3026      
Kristiina  Ojuland    RE         4067      
Liisa      Pakosta    IRL        2455      
Margus     Tsahkna    IRL        2534      
Marko      Mihkelson  RE         1504      
Mart       Laar       IRL        2711  
"""
fail = open("s6pru_l6ustaraamatus.txt","r")
erakonnad = []
re = 0
ke = 0
for rida in fail:
    # enimi, perenimi, erak, sobrad = rida.split(" ")
    poliitik = rida.split(" ")
    print(f"{poliitik[0]:10} {poliitik[1]:10} {poliitik[2]:4} {poliitik[3]}",end="")
    if poliitik[2]=="RE":
        re = re+1
    elif poliitik[2]=="KE":
        ke+=1
    if poliitik[2] not in erakonnad:
        erakonnad.append(poliitik[2])

    with open("poliitikud.txt", "a") as kirjutamiseks:
        kirjutamiseks.write(poliitik[0]+" "+poliitik[1]+"\n")
print()
print(f"Reformikad: {re} \nKesikuid: {ke}")
print(f"Erakondi kokku: {len(erakonnad)}")
fail.close