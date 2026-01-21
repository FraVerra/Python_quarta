'''
Parola più frequente

Leggere un file di testo e trovare la parola che compare più volte (ignorando maius-
cole/minuscole).

File articolo.txt:
Il gatto dorme sul divano.
Il cane corre nel giardino.
Il gatto e il cane sono amici.
Il gatto preferisce dormire.
'''

def frequenza(file):
    diz = {}
    parola_max = ""
    val_max = 0
    parole = file.lower().split()
    for dati in parole:
        dati = dati.strip(".")
        if dati in diz:
            diz[dati] += 1
        else:
            diz[dati] = 1
    cont = 0
    for dati in diz:
        if cont == 0:
            val_max = diz[dati]
            parola_max = dati
        else:
            if val_max < diz[dati]:
                val_max = diz[dati]
                parola_max = dati
        cont += 1
    print(f"frequenza massima: {val_max}   parola associata: {parola_max}")
        

def main():
    file = open("articolo.txt","r")
    contenuto = file.read()
    frequenza(contenuto)

if __name__ == "__main__":
    main()