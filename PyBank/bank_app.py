import os
from datetime import datetime 
from konverter_valuta import eurkn, kneur

racuni = {
}

transakcije = {
}

brojac_racuna = 1


def create_account():
    global racuni, brojac_racuna

    os.system('cls' if os.name == 'nt' else 'clear')

    print("#" * 95)
    print("Python Bank - Lakota Ivan".center(95))
    print("\n")
    print("KREIRANJE RAČUNA".center(95))
    print("_" * 95, "\n")

    broj_racuna = f"BA-{datetime.now().year}-{datetime.now().month:0>2}-{str(brojac_racuna):0>5}"

    naziv = input("\tUnesite naziv tvrtke: ")
    ulica_broj = input("\tUnesite ulicu i broj na kojem se nalazi sjedište tvrtke: ")
    grad = input("\tUnesite grad u kojem se nalazi sjedište tvrtke: ")
    postanski_broj = int(input("\tUnesite poštanski broj: "))
    oib = (input("\tUnesite OIB tvrtke: "))

    while len(oib) != 11:
        
        print("\n\tOIB mora imati točno 11 znamenki")
        oib = input("\tUnesite OIB tvrtke: ")
        print()

    for x in racuni:
        racun = racuni[x]
        if int(oib) == racun["oib"]:
            
            print("\n\tTvrtka s unesenim OIB-om već postoji u našoj bazi!")
            oib = input("\tUnesite točan OIB: ")
            print()

    valuta = input("\tOdaberite valutu računa (EUR/KN): ").upper()
    
    while valuta != "EUR" and valuta != "KN":
        
        print("\n\tOdabrite jednu od dvije valute: EUR/KN!")
        valuta = input("\tOdaberite valutu računa (EUR/KN): ").upper()

    ime_prezime = input("\tUnesite ime i prezime odgovorne osobe tvrtke: ")
    pocetni_polog = float(input("\tUnesite iznos koji želite položiti na račun: "))

    os.system('cls' if os.name == 'nt' else 'clear')

    print("#" * 95)
    print("Python Bank - Lakota Ivan".center(95))
    print("\n")
    print("KREIRANJE RAČUNA".center(95))
    print("_" * 95, "\n")

    print("\tUspješno ste stvorili račun", broj_racuna)

    oib = int(oib)
    racuni[broj_racuna] = {"naziv" : naziv, "adresa" : ulica_broj, "grad" : grad, "poštanski broj" : postanski_broj, "ime i prezime" : ime_prezime, "oib" : oib, "stanje" : round(pocetni_polog, 2), "valuta" : valuta }
    transakcije[broj_racuna] = []
    
    brojac_racuna += 1
    
    print("_"*95)
    input("\nPritisnite tipku <ENTER> za povratak na glavni izbornik...")

def update_acc():
    global racuni

    os.system('cls' if os.name == 'nt' else 'clear') 

    print("#" * 95)
    print("Python Bank - Lakota Ivan".center(95))
    print("\n")
    print("AŽURIRANJE RAČUNA".center(95))
    print("_" * 95, "\n")

    broj_racuna = input("\tUnesite broj računa: ").upper()

    if broj_racuna in racuni:

        racun = racuni[broj_racuna]

        print_podataka(racun)

        stavka = input("\n\tUnesite stavku koju bih ste promijenili: ").lower()

        if stavka in racun:
            
            if stavka == "naziv" or "ime i prezime":

                promjena = input("\tUnesite promjenu: ")

                racun[stavka] = promjena 

                os.system('cls' if os.name == 'nt' else 'clear') 

                print("#" * 95)
                print("Python Bank - Lakota Ivan".center(95))
                print("\n")
                print("AŽURIRANJE RAČUNA".center(95))
                print("_" * 95, "\n")
                print("\tUspješna promjena podatka!")
                print_podataka(racun)

            elif stavka == "adresa":

                ulica_broj = input("\tUnesite ulicu i broj: ")

                racun[stavka] = ulica_broj

                grad = input("\tUnesite ime grada u kojem se ulica nalazi: ")

                racun["grad"] = grad

                os.system('cls' if os.name == 'nt' else 'clear') 

                print("#" * 95)
                print("Python Bank - Lakota Ivan".center(95))
                print("\n")
                print("AŽURIRANJE RAČUNA".center(95))
                print("_" * 95, "\n")
                print("\tUspješna promjena podatka!")
                print_podataka(racun)

            elif stavka == "oib" or "poštanski broj":

                promjena = int(input("\tUnesite promjenu: "))

                racun[stavka] = promjena

                os.system('cls' if os.name == 'nt' else 'clear') 

                print("#" * 95)
                print("Python Bank - Lakota Ivan".center(95))
                print("\n")
                print("AŽURIRANJE RAČUNA".center(95))
                print("_" * 95, "\n")
                print("\tUspješna promjena podatka!")
                print_podataka(racun)
            
            elif stavka == "stanje":
                
                print("\n\tNe možete mijenjati stanje računa!")

            elif stavka == "valuta":

                if racun["valuta"] == "EUR":
                    
                    racun["valuta"] == "KN"

                else:
                    
                    racun["valuta"] == "EUR"
            
                os.system('cls' if os.name == 'nt' else 'clear') 

                print("#" * 95)
                print("Python Bank - Lakota Ivan".center(95))
                print("\n")
                print("AŽURIRANJE RAČUNA".center(95))
                print("_" * 95, "\n")
                print("Valuta promjenjena u", racun["valuta"])
                print_podataka(racun)
        
        else:

            print("\n\tStavka ne postoji u podacima!")

    else:

        print("\n\tRačun ne postoji u našoj banci.")

    print("_"*95)
    input("\nPritisnite tipku <ENTER> za povratak na glavni izbornik...")

def print_podataka(racun):
    global racuni
    
    print("\n\tPodaci o računu\n")
    print("\tNaziv tvrkte:", racun["naziv"])
    print("\tAdresa:", racun["adresa"])
    print("\tGrad:", racun["grad"])
    print("\tPoštanski broj:", racun["poštanski broj"])
    print("\tOIB tvrtke:", racun["oib"])
    print("\tValuta računa:", racun["valuta"])
    print("\tIme i prezime odgovorne osobe:", racun["ime i prezime"],"\n")
    print(f"\tStanje računa iznosi {racun['stanje']} {racun['valuta']}")


def transfer():
    global racuni

    os.system('cls' if os.name == 'nt' else 'clear') 

    print("#" * 95)
    print("Python Bank - Lakota Ivan".center(95))
    print("\n")
    print("UPLATA".center(95))
    print("_" * 95, "\n")

    racun_up = input("\tUnesite broj računa s kojeg vršite transfer: ").upper()
    racun_st = input("\tUnesite broj računa stjecatelja: ").upper()

    if racun_up and racun_st in racuni:

        if racun_up != racun_st:
            
            racun_up = racuni[racun_up]
            racun_st = racuni[racun_st]

            iznos = float(input(f"\n\tUnesite iznos koji želite prebaciti u {racun_up['valuta']}: "))
            
            if racun_up["valuta"] == "EUR" and racun_st["valuta"] == "KN":

                novi_iznos = eurkn(iznos)

            elif racun_up["valuta"] == "KN" and racun_st["valuta"] == "EUR":

                novi_iznos = kneur(iznos)

            if racun_up["valuta"] == racun_st["valuta"] and racun_up["stanje"] >= iznos:
            
                racun_up["stanje"] = round((racun_up["stanje"] - iznos), 2)
                racun_st["stanje"] = round((racun_st["stanje"] + iznos), 2)

                print("\n\tUspješna transakcija!")
            
                print_podataka(racun_up)
            
            elif racun_up["stanje"] >= iznos:

                racun_up["stanje"] = round((racun_up["stanje"] - iznos), 2)
                racun_st["stanje"] = round((racun_st["stanje"] + novi_iznos), 2)

                print("\n\tUspješna transakcija!")
            
                print_podataka(racun_up)

            else:
            
                print("\tNedovoljno sredstava na računu.")
        
        else:

            print("\tUnešeni brojevi računa su isti! Molimo pokušajte ponovno.")
    
    else:

        print("\n\tRačun ne postoji u našoj banci.")

    print("_" * 95)
    input("\nPritisnite tipku <ENTER> za povratak na glavni izbornik...") 


def prikaz_stanja():
    global racuni

    os.system('cls' if os.name == 'nt' else 'clear') 

    print("#" * 95)
    print("Python Bank - Lakota Ivan".center(95))
    print("\n")
    print("PRIKAZ STANJA RAČUNA".center(95))
    print("_" * 95, "\n")

    broj_racuna = input("\tUnesite broj računa: ").upper()

    if broj_racuna in racuni:
        
        racun = racuni[broj_racuna]
        
        print("\tStanje računa iznosi", round(racun["stanje"], 2), racun["valuta"])
        print_podataka(racun)
    
    else:
        
        print("\n\tRačun ne postoji u našoj banci.")

    print("_" * 95)
    input("\nPritisnite tipku <ENTER> za povratak na glavni izbornik...")  


def podizanje_polog():
    global racuni
    global transakcije

    os.system('cls' if os.name == 'nt' else 'clear')

    print("#" * 95)
    print("Python Bank - Lakota Ivan".center(95))
    print("\n")
    print("ISPLATA I PODIZANJE SREDSTAVA NA RAČUN".center(95))
    print("_" * 95, "\n")

    broj_racuna = input("\tUnesite broj računa: ").upper()

    if broj_racuna in racuni:
        racun = racuni[broj_racuna]

        print_podataka(racun)

        pod_pol = input("\n\tIzaberite opciju podizanje ili polog: ")

        if pod_pol == "podizanje":
            iznos = float(input("\tUnesite iznos koji želite podići: "))
        
            if iznos <= racun["stanje"]:
                novi_iznos = racun["stanje"] - iznos
                racun["stanje"] = round(novi_iznos, 2)
            
                print(f"\tUspješno ste podigli {round(iznos, 2)} {racun['valuta']}\n")
                print("\tNovo stanje računa iznosi", racun["stanje"], racun["valuta"])

                transakcije[broj_racuna].append(f"Vrijeme: {datetime.now()} -- Isplata: -{round(iznos, 2)} {racun['valuta']}")
        
            else:
                print("\tNedovoljno sredstava na računu.")    
        
        elif pod_pol == "polog":
            
            iznos = float(input("\tUnesite iznos koji želite položiti: "))
            novi_iznos = racun["stanje"] + iznos
            racun["stanje"] = round(novi_iznos, 2)
        
            print(f"\tUspješno ste položili {round(iznos, 2)} {racun['valuta']}\n")
            print("\tNovo stanje računa iznosi", racun["stanje"], racun["valuta"])

            transakcije[broj_racuna].append(f"Vrijeme: {datetime.now()} -- Uplata: +{round(iznos, 2)} {racun['valuta']}")

    else:
       
        print("\n\tRačun ne postoji u našoj banci.")

    print("_"*95)
    input("\nPritisnite tipku <ENTER> za povratak na glavni izbornik...")


def ispis_transakcija():
    global racuni
    global transakcije

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("#" * 95)
    print("Python Bank - Lakota Ivan".center(95))
    print("\n")
    print("ISPIS TRANSAKCIJA RAČUNA".center(95))
    print("_"  *95, "\n")

    broj_racuna = input("\tUnesite broj računa za pristup transakcijama: ").upper()

    if broj_racuna in racuni:

        racun = racuni[broj_racuna]

        print("\n\tTransakcije:", ",\n\t\t     ".join(transakcije[broj_racuna]))
        print_podataka(racun)
    
    else:
        
        print("\n\tRačun ne postoji u našoj banci.")

    print("_"*95)
    input("\nPritisnite tipku <ENTER> za povratak na glavni izbornik...") 


def glavni_izbornik():

    os.system('cls' if os.name == 'nt' else 'clear')

    print("#" * 95)
    print("Python Bank - Lakota Ivan".center(95))
    print("\n")
    print("GLAVNI IZBORNIK".center(95))
    print("_"*95)
    
    action = input("""
    (1) Izrada novog računa
    (2) Ažuriranje računa
    (3) Prikaz stanja postojećeg računa
    (4) Podizanje/polog sredstava na račun
    (5) Transfer sredstava sa računa
    (6) Ispis transakcija računa
    (7) Izlaz iz aplikacije

    Unesite broj: """ )

    if action == "1":
        create_account()
    elif action == "2":
        if racuni == {}:
            create_account()
        else:
            update_acc()
    elif action == "3":
        if racuni == {}:
            create_account()
        else:
            prikaz_stanja()
    elif action == "4":
        if racuni == {}:
            create_account()
        else:
            podizanje_polog()
    elif action == "5":
        if racuni == {}:
            create_account()
        else:
            transfer()
    elif action == "6":
        if racuni == {}:
            create_account()
        else:
            ispis_transakcija()
    elif action == "7":
        print("\nHvala na korištenju bankovne aplikacije!\n")
        quit()

while True:
    glavni_izbornik()

""" 
Almost done!
Prekontroliraj sve mogućnosti, popravi bugove
"""