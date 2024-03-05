#Agata Brete Jõpiselg

import tkinter
"""
1. TOPP SIKRET ehk Salatoimikute haldamise sĆ¼steem

EesmĆ¤rk: loo Pythoni ja Tkinteri abil rakendus, mis simuleerib "salatoimikute haldamise sĆ¼steemi". Rakendus peab vĆµimaldama kasutajal hallata eriti ohtlike isikute andmeid, sealhulgas inimese nime, isikukoodi, sĆ¼nniaega, sugu, pikemat infot/teksti ning pilti.

Funktsionaalsus:
* Andmete kuvamine: Rakendus kuvab olemasolevaid andmeid loetelus, kus kasutaja saab Ć¼ksikute kirjete peal klikkides vaadata tĆ¤psemat teavet.
* Andmete lisamine: Kasutaja saab lisada uusi isikuid andmebaasi, sisestades vajalikud andmed lĆ¤bi liidese.
* Andmete muutmine: Kasutaja saab olemasolevaid andmeid muuta, valides loetelust konkreetse kirje ja tehes vajalikud tĆ¤iendused vĆµi parandused.
* Andmete kustutamine: Kasutaja saab eemaldada kirjeid andmebaasist.
* Andmete hoiustamine: Andmeid hoitakse CSV, TXT vĆµi muus sobilikus failiformaadis, mis vĆµimaldab lihtsat andmete lisamist, muutmist ja kustutamist.

NĆµuded:
* Rakendus peab olema kasutajasĆµbralik ja intuitiivne.
* Andmete salvestamiseks ja lugemiseks tuleb kasutada failisĆ¼steemi (CSV, TXT vms).
* Rakendus peab vĆµimaldama piltide lisamist ja kuvamist koos isikute andmetega.
* Kasutajaliides peab olema loodud Tkinteri abil.
* Failid peavad olema kĆ¤ttesaadavad Githubis
"""


import tkinter as tk
from tkinter import messagebox, filedialog
import csv
from PIL import Image, ImageTk

class SalatoimikudRakendus:
    def __init__(self, root):
        self.root = root
        self.root.title("TOPP SIKRET - Salatoimikute Haldamise Süsteem")

        self.andmebaas = []
        self.loe_andmed()

        self.loo_kasutajaliides()
    
    def loe_andmed(self):
        try:
            with open("salatoimikud.csv", "r", newline="") as file:
                reader = csv.reader(file)
                for rida in reader:
                    self.andmebaas.append(rida)
        except FileNotFoundError:
            messagebox.showerror("Viga", "Andmebaasi faili ei leitud.")
    
    def kirjuta_andmed(self):
        with open("salatoimikud.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.andmebaas)
    
    def lisa_isik(self):
        nimi = self.nimi_sisestus.get()
        isikukood = self.isikukood_sisestus.get()
        synniaeg = self.synniaeg_sisestus.get()
        sugu = self.sugu_sisestus.get()
        info = self.info_sisestus.get("1.0", tk.END).strip()
        piltitee = self.piltitee_sisestus.get()
        
        uus_isik = [nimi, isikukood, synniaeg, sugu, info, piltitee]
        self.andmebaas.append(uus_isik)
        self.kirjuta_andmed()
        self.naita_andmed()
        self.kustuta_sisestus()
    
    def muuda_isikut(self):
        valitud_indeks = self.andmete_loetelu.curselection()
        if valitud_indeks:
            valitud_indeks = valitud_indeks[0]
            self.andmebaas[valitud_indeks] = [
                self.nimi_sisestus.get(),
                self.isikukood_sisestus.get(),
                self.synniaeg_sisestus.get(),
                self.sugu_sisestus.get(),
                self.info_sisestus.get("1.0", tk.END).strip(),
                self.piltitee_sisestus.get()
            ]
            self.kirjuta_andmed()
            self.naita_andmed()
            self.kustuta_sisestus()
        else:
            messagebox.showerror("Viga", "Palun valige isik muutmiseks.")

    def kustuta_isik(self):
        valitud_indeks = self.andmete_loetelu.curselection()
        if valitud_indeks:
            valitud_indeks = valitud_indeks[0]
            self.andmebaas.pop(valitud_indeks)
            self.kirjuta_andmed()
            self.naita_andmed()
            self.kustuta_sisestus()
        else:
            messagebox.showerror("Viga", "Palun valige isik kustutamiseks.")
    
    def naita_andmed(self):
        self.andmete_loetelu.delete(0, tk.END)
        for isik in self.andmebaas:
            self.andmete_loetelu.insert(tk.END, isik[0])
    
    def naita_valitud_isiku_andmed(self, event):
        valitud_indeks = self.andmete_loetelu.curselection()
        if valitud_indeks:
            valitud_indeks = valitud_indeks[0]
            isik = self.andmebaas[valitud_indeks]
            self.kustuta_sisestus()
            self.nimi_sisestus.insert(tk.END, isik[0])
            self.isikukood_sisestus.insert(tk.END, isik[1])
            self.synniaeg_sisestus.insert(tk.END, isik[2])
            self.sugu_sisestus.insert(tk.END, isik[3])
            self.info_sisestus.insert(tk.END, isik[4])
            self.piltitee_sisestus.insert(tk.END, isik[5])
            # Kuvame ka pildi
            if isik[5]:
                pilt = Image.open(isik[5])
                pilt.thumbnail((100, 100))
                self.kuva_pilt = ImageTk.PhotoImage(pilt)
                self.pilt_kuva.config(image=self.kuva_pilt)
                self.pilt_kuva.image = self.kuva_pilt

    def kuvaa_pilt(self, event):
        valitud_indeks = self.andmete_loetelu.curselection()
        if valitud_indeks:
            valitud_indeks = valitud_indeks[0]
            isik = self.andmebaas[valitud_indeks]
            if isik[5]:
                pilt = Image.open(isik[5])
                pilt.thumbnail((200, 200))
                suurendatud_pilt = ImageTk.PhotoImage(pilt)
                tk.messagebox.showinfo("Pilt", image=suurendatud_pilt)

    def kustuta_sisestus(self):
        self.nimi_sisestus.delete(0, tk.END)
        self.isikukood_sisestus.delete(0, tk.END)
        self.synniaeg_sisestus.delete(0, tk.END)
        self.sugu_sisestus.delete(0, tk.END)
        self.info_sisestus.delete("1.0", tk.END)
        self.piltitee_sisestus.delete(0, tk.END)

    def lisa_pilt(self):
        piltitee = filedialog.askopenfilename()
        self.piltitee_sisestus.delete(0, tk.END)
        self.piltitee_sisestus.insert(tk.END, piltitee)

    def loo_kasutajaliides(self):
        nimi_silt = tk.Label(self.root, text="Nimi:")
        nimi_silt.grid(row=0, column=0, sticky="w")
        self.nimi_sisestus = tk.Entry(self.root)
        self.nimi_sisestus.grid(row=0, column=1, padx=5, pady=5)

        isikukood_silt = tk.Label(self.root, text="Isikukood:")
        isikukood_silt.grid(row=1, column=0, sticky="w")
        self.isikukood_sisestus = tk.Entry(self.root)
        self.isikukood_sisestus.grid(row=1, column=1, padx=5, pady=5)

        synniaeg_silt = tk.Label(self.root, text="Sünniaeg:")
        synniaeg_silt.grid(row=2, column=0, sticky="w")
        self.synniaeg_sisestus = tk.Entry(self.root)
        self.synniaeg_sisestus.grid(row=2, column=1, padx=5, pady=5)

        sugu_silt = tk.Label(self.root, text="Sugu:")
        sugu_silt.grid(row=3, column=0, sticky="w")
        self.sugu_sisestus = tk.Entry(self.root)
        self.sugu_sisestus.grid(row=3, column=1, padx=5, pady=5)

        info_silt = tk.Label(self.root, text="Info:")
        info_silt.grid(row=4, column=0, sticky="w")
        self.info_sisestus = tk.Text(self.root, height=4, width=30)
        self.info_sisestus.grid(row=4, column=1, padx=5, pady=5)

        piltitee_silt = tk.Label(self.root, text="Pildi tee:")
        piltitee_silt.grid(row=5, column=0, sticky="w")
        self.piltitee_sisestus = tk.Entry(self.root)
        self.piltitee_sisestus.grid(row=5, column=1, padx=5, pady=5)

        self.andmete_loetelu = tk.Listbox(self.root, width=40)
        self.andmete_loetelu.grid(row=0, column=2, rowspan=6, padx=5, pady=5)
        self.andmete_loetelu.bind("<<ListboxSelect>>", self.naita_valitud_isiku_andmed)
        self.andmete_loetelu.bind("<Double-Button-1>", self.kuvaa_pilt)

        self.pilt_kuva = tk.Label(self.root)
        self.pilt_kuva.grid(row=6, column=0, columnspan=2)

        self.lisa_nupp = tk.Button(self.root, text="Lisa", command=self.lisa_isik)
        self.lisa_nupp.grid(row=7, column=0, padx=5, pady=5, sticky="ew")

        self.muuda_nupp = tk.Button(self.root, text="Muuda", command=self.muuda_isikut)
        self.muuda_nupp.grid(row=7, column=1, padx=5, pady=5, sticky="ew")

        self.kustuta_nupp = tk.Button(self.root, text="Kustuta", command=self.kustuta_isik)
        self.kustuta_nupp.grid(row=7, column=2, padx=5, pady=5, sticky="ew")

        self.naita_andmed()

if __name__ == "__main__":
    root = tk.Tk()
    rakendus = SalatoimikudRakendus(root)
    root.mainloop()



