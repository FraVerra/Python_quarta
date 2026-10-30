'''
Playlist
Un dizionario associa nomi di playlist a liste di titoli di canzoni. Scrivere funzioni per:
(a) contare le canzoni totali, (b) cercare in quale playlist si trova una canzone, (c) unire
due playlist in una nuova.
playlist = {
"Rock": ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"],
"Pop": ["Thriller", "Like a Prayer", "Billie Jean"],
"Relax": ["Hotel California", "Imagine", "Let It Be"]
}
'''

def contare(lista):
    cont = 0
    for dati in lista:
        for valori in lista[dati]:
            cont += 1
    return cont

def cercare(lista):
    nome = input("inserisci il nome della canzone: ")
    nome_playlist = []
    for dati in lista:
        for valori in lista[dati]:
            if valori == nome:
                nome_playlist.append(dati)
    return nome_playlist

def unire(lista):
    nuova_playlist = {}
    nuove_canzoni = []
    titolo = "Caso"
    cont = 0
    for dati in lista:
        if cont < 6:
            nuove_canzoni.append(lista[dati])
            cont += 3
    nuova_playlist[titolo]=nuove_canzoni
    print(nuova_playlist)

def main():

    playlist = {
        "Rock": ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"],
        "Pop": ["Thriller", "Like a Prayer", "Billie Jean"],
        "Relax": ["Hotel California", "Imagine", "Let It Be"]
        }   

    print(f"numero totale di playlist = {contare(playlist)}")
    nome_playlist = cercare(playlist)
    if len(nome_playlist) == 0:
        print("nessuna canzone trovata...")
    else:
        print(f"nome/i playlist: {nome_playlist}")
    unire(playlist)
if __name__ == "__main__":
    main()