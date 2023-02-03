class Autok:
    def __init__(self, lista):
        self.nev = lista[0]
        self.gyar_datum = int(lista[1])

    def __str__(self):
        return f"{self.nev}, {self.gyar_datum}"