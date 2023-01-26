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