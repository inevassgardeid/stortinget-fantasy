from politiker import Politiker
import json


fil = open("politiker.json")
data = json.load(fil)
fil.close()
politikere = []

for politiker in data["representanter_oversikt"]["representanter_liste"]["representant"]:
    ny = Politiker(politiker["fornavn"], politiker["etternavn"], politiker["parti"]["navn"])
