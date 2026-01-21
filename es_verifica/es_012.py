'''
Catalogo libri
Una lista contiene dizionari con chiavi titolo, autore, anno, prezzo. Scrivere funzioni
per: (a) cercare libri di un autore, (b) calcolare il prezzo medio, (c) trovare il libro più
recente.
libri = [
{"titolo": "Il nome della rosa", "autore": "Umberto Eco", "anno": 1980, "prezzo": 15.50},
{"titolo": "1984", "autore": "George Orwell", "anno": 1949, "prezzo": 12.00},
{"titolo": "Il pendolo di Foucault", "autore": "Umberto Eco", "anno": 1988, "prezzo": 18.00},
{"titolo": "Fahrenheit 451", "autore": "Ray Bradbury", "anno": 1953, "prezzo": 11.50},
{"titolo": "Il mondo nuovo", "autore": "Aldous Huxley", "anno": 1932, "prezzo": 13.00}
]
'''

def cerca_libro(lista):
    nome_libro = input("inserisci il nome del libro: ")
    for libro in lista:
        if libro["autore"] == nome_libro:
            return libro                      

def calcolo_prezzo(lista):
    n_libri = 0
    somma_prezzi = 0.0
    for dati in lista:
        cont = 0
        for valori in dati:
            if cont == 3:
                n_libri += 1
                somma_prezzi += dati[valori]
            cont += 1
    return somma_prezzi/n_libri

def libro_recente(lista):
    data_recente = 0
    cont = 0
    y = 0
    for dati in lista:
        cont = 0
        for valori in dati:
            if y == 0:
                data_recente = dati[valori]
            elif cont == 2:
                if data_recente < dati[valori]:
                    data_recente = dati[valori]
            cont += 1
        y += 1
    print(data_recente)


def main():
    libri = [
        {"titolo": "Il nome della rosa", "autore": "Umberto Eco", "anno": 1980, "prezzo": 15.50},
        {"titolo": "1984", "autore": "George Orwell", "anno": 1949, "prezzo": 12.00},
        {"titolo": "Il pendolo di Foucault", "autore": "Umberto Eco", "anno": 1988, "prezzo": 18.00},
        {"titolo": "Fahrenheit 451", "autore": "Ray Bradbury", "anno": 1953, "prezzo": 11.50},
        {"titolo": "Il mondo nuovo", "autore": "Aldous Huxley", "anno": 1932, "prezzo": 13.00}
    ]
    trovato = cerca_libro(libri)
    if trovato:
        print("libro trovato!")
    else:
        print("libro non trovato...")
    
    print(f"la media dei prezzi è: {calcolo_prezzo(libri)}")
    libro_recente(libri)

if __name__ == "__main__":
    main()