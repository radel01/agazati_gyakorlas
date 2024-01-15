class Park:

    def __init__(self, ev, aszam, latogatas, atlag):
        self.ev = int(ev)
        self.aszam = int(aszam)
        self.latogatas = int(latogatas)
        self.atlag = float(atlag.replace(",","."))

    def __str__(self):
        return f"Év {self.ev},  állatkert, vadaspark, kultúrpark száma: {self.aszam}, látogatások száma: {self.latogatas}, látogatások átlagos száma: {self.atlag}."
