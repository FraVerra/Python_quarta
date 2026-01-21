'''
Numeri da file
Un file contiene un numero intero per riga. Leggere il file e calcolare: somma, media,
minimo e massimo.
File numeri.txt:
45
23
67
12
89
34
56
'''

file = open("numeri.txt","r")
contenuto = file.read()
righe = contenuto.split("\n")
numeri = []
for dati in righe:
    numeri.append(int(dati))
somma = sum(numeri)
print(f"somma = {somma}")

cont = 0
n = 0
media = 0
min = 0
max = 0
for dati in numeri:
    media += dati
    n += 1
    if cont == 0:
        min = dati
        max = dati
    elif min > dati:
        min = dati
    elif max < dati:
        max = dati
    cont+=1
print(f"media dei valori: {media/n}    numero massimo: {max}   numero minimo: {min}")