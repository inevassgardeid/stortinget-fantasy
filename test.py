from politiker import Politiker
from lag import Lag
import json

fil = open("politiker.json")
data = json.load(fil)
fil.close()

politikere = []

for politiker in data["representanter_oversikt"]["representanter_liste"]["representant"]:
    ny = Politiker(politiker["fornavn"], politiker["etternavn"], politiker["parti"]["navn"])
    politikere.append(ny)
    # politikere.append({
    #     "fornavn": politiker["fornavn"],
    #     "etternavn": politiker["etternavn"],
    #     "parti": politiker["parti"]["navn"]
    # })

thorsLag = Lag("Thors lag")
thorsLag.kjop_politiker(politikere[0])
thorsLag.hent_lag()
print("ferdig")
