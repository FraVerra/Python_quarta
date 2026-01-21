'''
Scrivere una funzione che trovi il secondo valore più grande in una lista di numeri (senza
usare sort o sorted).
valori = [45, 12, 78, 34, 67, 23, 89, 56]
'''

def controllo(lista):
    massimo = lista[0]
    for v in valori:
        if v > massimo:
            massimo = v
    
    secondoMax = lista[0]
    for v in lista:
        if (v > secondoMax) and (v != massimo):
            secondoMax = v
    return secondoMax

def inserire():
    lista = []
    lista = input("inserisci tot numeri: ")
    return lista

def main():
    lista = []
    lista = inserire()
    secondoMax = controllo(lista)
    print(secondoMax)

if __name__ == "__main__":
    main()