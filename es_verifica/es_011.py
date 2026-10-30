'''
Unione di dizionari
Dati due dizionari, crearne uno nuovo che contenga tutte le chiavi. Se una chiave è
presente in entrambi, sommare i valori.
vendite_gennaio = {"mele": 120, "pere": 85, "arance": 200}
vendite_febbraio = {"mele": 95, "banane": 150, "arance": 180}
'''
def somma_dizionari(diz1, diz2):
    diz_somma = {}
    for dati in diz1:
        diz_somma[dati] = diz1[dati]
    for dati in diz2:
        if dati in diz_somma:
            diz_somma[dati] += diz2[dati]
        else:
            diz_somma[dati] = diz2[dati]
    print(diz_somma)

def main():
    diz1 = {"mele": 120, "pere": 85, "arance": 200}
    diz2 = {"mele": 95, "banane": 150, "arance": 180}
    somma_dizionari(diz1, diz2)


if __name__ == "__main__":
    main()

