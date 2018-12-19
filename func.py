# Main class


class Vozilo:
    tip = ""
    znamka = ""
    model = ""
    km = 0.0
    datum_servisa = ""

    def __init__(self, tip, znamka, model, km, datum_servisa):
        self.tip = tip
        self.znamka = znamka
        self.model = model
        self.km = km
        self.datum_servisa = datum_servisa

    def dodajanje_km(self, novi_km):
        self.km = self.km + float(novi_km)
        return self.km

    def sprememba_datuma(self, datum):
        self.datum_servisa = datum
        return self.datum_servisa


# class_variables
tovornjak = Vozilo("Tovornjak", "MAN", "XY12", 100.121, "1.9.2017")
avto = Vozilo("Avto", "VW", "Caddy", 243.247, "3.10.2018")
kombi = Vozilo("Kombi", "MB", "Vito", 109.555, "1.9.2017")
vilicar = Vozilo("Vilicar", "Toyota", "Long", 1.297, "Ni servisa - kupljen 1.12.2018")
seznam = [tovornjak, avto, kombi, vilicar]

izbrano_p = 0
podatki = "%s - %s %s" % (seznam[int(izbrano_p)-1].tip, seznam[int(izbrano_p)-1].znamka, seznam[int(izbrano_p)-1].model)
