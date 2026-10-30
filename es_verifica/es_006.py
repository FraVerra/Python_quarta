'''
Rimozione duplicati
Data una lista, restituire una nuova lista contenente gli stessi elementi ma senza duplicati,
mantenendo l’ordine di prima apparizione.
elementi = ["mela", "pera", "mela", "banana", "pera", "arancia", "mela"]
'''

def controllo(lista):
    listaCorretta = []
    count = 0
    listaParole = lista.split(" ")
    for parole in listaParole:
        if count == 0:
            listaCorretta.append(parole)
        elif count != 0:
            if parole not in listaCorretta:
                listaCorretta.append(parole)
        count+=1
    print(listaCorretta)

def inserire():
    lista = input("inserisci tot parole : ")
    return lista

def main():
    lista = inserire()
    controllo(lista)

if __name__ == "__main__":
    main()