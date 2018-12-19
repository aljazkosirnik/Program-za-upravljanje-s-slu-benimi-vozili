from func import *

print "Dobrodosli v program za upravljane sluzbenih vozil \n Moznosti: "


def main():
    print " (1)Ogled seznama vozil \n (2)Urejanje KM \n (3)Urejanje datum servisa \n (4)Dodati novo vozilo \n (5)Izbrisati vozilo \n (6)Zapreti program"
    print "\t"
    zelja = raw_input(" Kaj zelis storiti?")
    print "\t"

    if zelja == "1":  # Ogled seznama vozil
        print_vozila()

    elif zelja == "2":  # Urejanje KM
        print_vozila()
        izbrano_km = raw_input("Kateremu vozilu zelis dodati kilometre?: ")
        print "Trenutno ima %s %s kilometrov." % (podatki, seznam[int(izbrano_km)-1].km)
        kolicina = raw_input("Koliko kilometrov dodajas? ")
        try:
            print "Sedaj ima %s %s kilometrov." % (podatki, seznam[int(izbrano_km)-1].dodajanje_km(float(kolicina)))
        except ValueError:
            print "Prosim vnesite stevilko"

    elif zelja == "3":  # Urejanje datum servisa
        print_vozila()
        izbrano_d = raw_input("Kateremu vozilu zelis spremeniti datum zadnjega servisa?: ")
        print "Zadnji servis je %s imel %s." % (podatki, seznam[int(izbrano_d) - 1].datum_servisa)
        datum = raw_input("Prosim vnesi nov datum: ")
        print "Sedaj ima %s nov datum servisa %s." % (podatki, seznam[int(izbrano_d) - 1].sprememba_datuma(datum))

    elif zelja == "4":  # Dodati novo vozilo
        print "Vnesi podatke novega vozila"
        nov_tip = raw_input("Vnesi tip vozila (kombi, avto, vilicar..): ")
        nov_znamka = raw_input("Znamka vozila: ")
        nov_model = raw_input("Model vozila: ")
        nov_km = raw_input("KM vozila: ")
        nov_datum = raw_input("Datum zadnjega servisa: ")
        nov_tip = Vozilo(nov_tip, nov_znamka, nov_model, float(nov_km), nov_datum)
        seznam.append(nov_tip)
        p = len(seznam) - 1
        print "Dodal si %s %s - %s" % (seznam[p].tip, seznam[p].znamka, seznam[p].model)

    elif zelja == "5":  # Izbrisati vozilo
        print_vozila()
        izbrano = raw_input("Katero vozilo zelis izbrisati?: ")
        print "Izbrisan %s %s %s." % (seznam[int(izbrano) - 1].tip, seznam[int(izbrano) - 1].znamka, seznam[int(izbrano) - 1].model)
        del seznam[int(izbrano)-1]

    elif zelja == "6":  # Zapreti program
        exit()

    else:  # reset
        print "Napaka, izberi funkcijo med 1 in 6"


def print_vozila():
    i = 0
    while i < len(seznam):
        print "%s  -  %s %s %s, ki ima %s kilometrov in je imel servis %s" % (int(seznam.index(seznam[i]) + 1), seznam[i].tip, seznam[i].znamka, seznam[i].model, seznam[i].km, seznam[i].datum_servisa)
        i += 1
    print "\t"


while True:
    main()
