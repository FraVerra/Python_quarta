numeri = []
pari = []
somma = 0
cont = 0
max = 0
min = 0
numeri.append(input("inserisci numeri separati da spazi: "))
for campi in numeri:
    for dati in campi:
        print(dati)
'''
        numero = int(dati)        
        if numero > max:
            max = numero
        elif dati < min:
            min = numero
        cont+=1
        somma+=numero
        if numero % 2 == 0:
            pari.append(numero)
'''
print(f"media: {somma/cont}")
print(f"numeri pari: {pari}")
print(f"massimo: {max}\nminimo: {min}")
