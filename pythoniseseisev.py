#Agata Brete Jõpiselg
#12.18
"""
Meil on vaja transportida teatud arv inimesi mingi arvu identsete bussidega. Eeldame, et reisijaid
on vähemalt üks. Koostada programm, mis küsib transporditavate inimeste arvu ja ühe bussi
kohtade arvu (just sellises järjekorras) ning väljastab ekraanile, mitu bussi on vaja ja mitu
inimest on viimases bussis (eeldusel, et kõik eelnevad bussid on täis).
Võib-olla on abi nendest tehetest
● // täisarvuline jagamine, 36 // 10 → 3

● % jäägi leidmine 36 % 10 → 6
Testige oma programmi muuhulgas järgmiste algandmetega:
● inimeste arv: 60, kohtade arv: 40;
● inimeste arv: 80, kohtade arv: 40;
● inimeste arv: 20, kohtade arv: 40;
● inimeste arv: 40, kohtade arv: 40.
Püüdke ka mõista, miks just sellised testandmed valiti.
"""
def arvutabussid(inimestearv, kohtadearv):
    bussidearv = inimestearv // kohtadearv
    jaak = inimestearv % kohtadearv
    
    if jaak > 0:
        bussidearv += 1
    
    print(f"Vaja läheb {bussidearv} bussi.")
    
    if jaak > 0:
        print(f"Viimases bussis on {jaak} inimest.")
    else:
        print("Viimases bussis on kõik kohad täidetud.")


arvutabussid(60, 40)
arvutabussid(80, 40)
arvutabussid(20, 40)
arvutabussid(40, 40)

#Miks on valitud sellised testandmed?
# Need testid katavad erinevaid stsenaariume ja aitavad veenduda, et programm töötab
#õigesti erinevate siseandmetega

"""
Pilvede alumise pinna (aluse) kõrguse järgi liigitatakse pilvi ülemise, keskmise ja alumise kihi
pilvedeks. Ülemiste pilvede alus on kõrgemal kui 6 km, keskmistel pilvedel on 2-6 km kõrgusel,
alumistel pilvedel on madalamal kui 2 km. Koostada programm, mis
● küsib kasutajalt pilvede aluse kõrgust (kilomeetrites),
● väljastab ekraanile Need on ülemised pilved, kui sisestatu on üle 6,0 km,
● väljastab Need ei ole ülemised pilved, kui kõrgus on 6,0 km või alla selle.
Kasutaja peab saama sisestada pilvede kõrgust nii täisarvuna kui ka ujukomaarvuna, nt 7.5.
"""
def main():
    try:
        
        korgus = float(input("Sisesta pilvede aluse kõrgus kilomeetrites: "))

        if korgus > 6.0:
            print("Need on ülemised pilved.")
        else:
            print("Need ei ole ülemised pilved.")
    except ValueError:
        print("Vigane sisend. Palun sisesta number.")

if __name__ == "__main__":
    main()


"""
Koostada programm, mille
● 1. real luuakse muutuja nimega aasta ning antakse sellele väärtuseks 2020 (arvuna);
● 2. real luuakse muutuja nimega liblikas ning antakse sellele väärtuseks &quot;teelehe-
mosaiikliblikas&quot; (sõnena);
● 3. real luuakse muutuja nimega lause_keskosa ning antakse sellele väärtuseks &quot;. aasta
liblikas on &quot; (sõnena);
● 4. real luuakse muutuja nimega lause, mille väärtuse saamiseks ühendatakse üheks
sõnaks muutujad aasta, lause_keskosa ja liblikas (vajadusel tuleb kasutada funktsiooni,
mis teisendab arvu sõneks);
● 5. real väljastatakse muutuja lause väärtus ekraanile.
"""
aasta = 2020

liblikas = "teelehemosaikliblikas"

lausekeskosa = ". aasta liblikas on "
lause = str(aasta) + lausekeskosa + liblikas

print(lause)
"""
Koostada programm, mis väljastaks ekraanile teksti Tere, maailm! täpselt sellisel kujul
- koma ja hüüumärgiga.
"""
print(f"Tere, maailm")

