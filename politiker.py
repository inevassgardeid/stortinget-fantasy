from politiker import Politiker
import json


fil = open("politiker.json")
data = json.load(fil)
fil.close()
politikere = []

for politiker in data["representanter_oversikt"]["representanter_liste"]["representant"]:
    ny = Politiker(politiker["fornavn"], politiker["etternavn"], politiker["parti"]["navn"])

class Politiker:
    def __init__(self, fornavn, etternavn, parti):
        self._fornavn = fornavn
        self._etternavn = etternavn
        self._parti = parti

    def hent_politiker(self):
        pass

    def hent_verdi(self, verdi):
        self._verdi = verdi
        Politiker()