from politiker import Politiker

class Lag:
    def __init__(self, lagnavn):
        self._lagnavn = lagnavn
        self._lag = []
        self._saldo = 10000

    def hent_lag(self):
        return self._lag

    def kjop_politiker(self, politiker):
        self._politiker = politiker 
        self._lag.append(politiker)
        self._saldo -= 1000
    
    def selg_politiker(self, politiker):
        self._politiker = politiker
        self._lag.pop(politiker)
        self._saldo += 1000