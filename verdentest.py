from verden import Verden
from verden import politikere 
from politiker import Politiker
from lag import Lag

politikere = politikere

min_verden = politikere

for politiker in politikere:
    ny_politiker = Politiker("Støre")
    min_verden.append(ny_politiker)

mitt_lag = Lag("Nasjonal Blanding")
mitt_lag.kjop_politiker(Verden.finn_politiker("Støre"))
mitt_lag.kjop_politiker(Verden.finn_politiker("Solberg"))
print(mitt_lag)
