print(f"I/A: ")
import bevezeto
print(f"\t {bevezeto.auto_neve} {bevezeto.gyartasi_datum} ")
print(f" I/B: ")
bevezeto.kiir()
import sorozat
print("II/A,B,C: ")
sorozat.veletlen_szam()
sorozat.elvalaszt()
print(f"II/D,E: \n \t Az egyjegyűek száma: {sorozat.egyjegyu_szam()} ")
import auto
auto.beolvas()
print(f"III/Flotta \n \t Autók száma: {auto.flotta()}")
auto.legfiatalabb()
print(f"III/Legfiatalabb: \n \t A legfiatalabb autó: {auto.auto_lista[auto.legfiatalabb()].nev} ({auto.auto_lista[auto.legfiatalabb()].gyar_datum})")