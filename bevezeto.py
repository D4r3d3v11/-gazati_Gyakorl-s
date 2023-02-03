auto_neve = input(f" \t Autó neve: ")
gyartasi_datum = int(input(f" \t Gyartasi dátum: "))

def kiir():
   if gyartasi_datum < 2000:
       print(f"Ez az {auto_neve} Öreg autó")
   elif gyartasi_datum >= 2000 and gyartasi_datum < 2023:
       print(f"Ez az {auto_neve} Átlagos koru")
   elif gyartasi_datum == 2023:
       print(f"Ez az {auto_neve} Friss gyártás")
   else:
       print("Hibás adat")





