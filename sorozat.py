import random
lottoszam_lista = []
def veletlen_szam():
    i = 0
    while i <= 5:
        szam = random.randint(1, 100)
        lottoszam_lista.append(szam)
        i += 1
def elvalaszt():
    i = 0
    szoveg = ""
    while i < len(lottoszam_lista):
        if i == 0:
            szoveg = str(lottoszam_lista[i])
        else:
            szoveg += "-" + str(lottoszam_lista[i])
        i += 1
    print(szoveg)
def egyjegyu_szam():
    i = 0
    egesz_szam = 0
    while i < len(lottoszam_lista):
        if lottoszam_lista[i] < 10 and lottoszam_lista[i] > 0:
            egesz_szam += 1
        i += 1
    file_kiir(egesz_szam)
    return egesz_szam

def file_kiir(egesz_szam):
    f = open("szamok.txt", "w", encoding="utf-8")
    beir = egesz_szam
    f.write(f"Az egyjegyűek száma: {beir}")
    f.close()
    print("Elkészült a file kiirás")
