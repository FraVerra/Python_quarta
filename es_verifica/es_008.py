'''
Contatore di caratteri
Data una stringa, costruire un dizionario che associ a ogni carattere il numero di volte
che compare.
testo = "abracadabra"
'''

def inserire():
    stringa = input("inserisci una stringa: ")
    return stringa

def controllo(stringa):
    diz = {}
    for lettera in stringa:
        if lettera in diz:
            diz[lettera] = diz[lettera]+1
        else:
            diz[lettera]=1
    print(diz)

def main():
    stringa = inserire()
    controllo(stringa)

if __name__ == "__main__":
    main()