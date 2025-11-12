#ora vediamo come andare ad inserire dei numeri

intero = int(input("inserisci un numero intero:\t"))
print(f"\nhai inserito: {intero} che è una variabile di tipo {type(intero)}")

decimale = float(input("inserisci un numero decimale:\t"))
print(f"\nhai inerito : {decimale} che è una variabile di tipo {type(decimale)}")

somma = decimale + intero

print(f"la somma tra i due numeri è: {somma} che è una variabile di tipo {type(decimale)}")