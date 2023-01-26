from verden import Verden
class Lag:
    def __init__(self, lagnavn):
        self._lagnavn = lagnavn
        self._lag = []
        self._saldo = 10000

    def hent_lag(self):
        return self._lag

    def kjop_politiker(self):
        Verden.legg_til_politiker() 
        self._saldo -= 1000

        return Verden(self.lag)
    
    def selg_politiker(self):
        Verden.legg_til_politiker() 
        self._saldo += 1000

        return Verden(self.lag)
