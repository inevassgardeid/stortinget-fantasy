from verden import Verden
from politiker import Politiker
from lag import Lag

min_verden = Verden()

for politiker in politikerliste:
    ny_politiker = Politiker(navn, parti)
    min_verden.append(ny_politiker)

mitt_lag = Lag("Nasjonal Blanding")
mitt_lag.kjop(finn_politiker("Jonas Gahr Støre"))