from Autok import Autok

auto_lista = []

def beolvas():
    f = open("auto.txt", "r", encoding="utf-8")
    f.readline()
    auto = f.readlines()
    f.close()
    feldolgoz(auto)
def feldolgoz(auto):
    i = 0
    while i < len(auto):
        lista = auto[i].strip().split("$")
        autok = Autok(lista)
        auto_lista.append(autok)
        i += 1

def flotta():
    return len(auto_lista)

def legfiatalabb():
    i = 0
    legfiatalabb = 0
    while i < len(auto_lista):
        if auto_lista[legfiatalabb].gyar_datum < auto_lista[i].gyar_datum:
            legfiatalabb = i
        i += 1
    return legfiatalabb
