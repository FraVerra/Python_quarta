'''
Pari e dispari
Data una lista di interi, scrivere una funzione che restituisca due liste separate: una con
i numeri pari e una con i dispari.
numeri = [3, 8, 12, 7, 2, 15, 20, 9, 4]
'''

def pariDispari(lista):
    pari = []
    dispari = []
    for numeri in lista:
        if numeri != " ":
            numero = int(numeri)
            if numero % 2 == 0:
                pari.append(numero)
            else:
                dispari.append(numero)
    return pari, dispari

def inserisci():
    lista = []
    lista = input("inserisci n numeri da controllare: ")
    return lista

def main():
    lista = inserisci()
    pari,dispari = pariDispari(lista)
    print(f"pari : {pari}")
    print(f"dispari : {dispari}")

if __name__ == "__main__":
    main()

