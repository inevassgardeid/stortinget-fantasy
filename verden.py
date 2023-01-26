import json
from politiker import Politiker

fil = open("politiker.json")
data = json.load(fil)
fil.close()
politikere = []

for politiker in data["representanter_oversikt"]["representanter_liste"]["representant"]:
    verden = politiker["fornavn"], politiker["etternavn"], politiker["parti"]["navn"]

    politikere.append(verden)

print(politikere)

class Verden: 
    def __init__(self):
        self.politikere = politikere
        self.lag = []

    def finn_politiker(self):
        for etternavn in politikere:
            if etternavn == ["etternavn"]:
                return Politiker(["fornavn"], ["etternavn"], ["parti"])

    def legg_til_politiker(self):
        for etternavn in politikere:
            if etternavn == ["etternavn"]:
                self.lag.append(Politiker(["fornavn"], ["etternavn"], ["parti"]))

    def legg_til_lag(self):
        pass