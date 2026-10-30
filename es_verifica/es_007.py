'''
Date due liste, restituire una nuova lista con gli elementi presenti in entrambe.
lista_a = [1, 5, 8, 12, 15, 20]
lista_b = [3, 5, 10, 12, 18, 20, 25]
'''

def inserire():
    lista1 = input("inserisci i valori della prima lista: ")
    lista2 = input("inserisci i valori della seconda lista: ")
    return lista1, lista2

def controllo(lista1, lista2):
    lista1Corretta = lista1.split(" ")
    lista2Corretta = lista2.split(" ")
    listaFinale = []
    for numero in lista1Corretta:        
        if numero != " ":
            if numero in lista2Corretta:
                listaFinale.append(numero)
    return listaFinale

def main():
    lista1, lista2 = inserire()
    listaFinale = controllo(lista1, lista2)
    print(listaFinale)

if __name__ == "__main__":
    main()