'''
Scrivi un programma che legge il file promessi_sposi.txt, 
conta quante volte compare la parola “Renzo” (case-insensitive), 
trova la prima riga in cui appare e salva il totale in statistiche.txt.
'''
def lettura_file():
    file = open("es_002_promessi_sposi.txt","r")
    return file.readlines()

def conta_parole(file):
    cont_parole = 1
    cont_righe = 1
    for righe in file:
        parole = righe.split(" ")
        for dati in parole:
            if dati.lower() == "renzo":
                cont_parole+=1
            cont_righe+=1
    return cont_parole/cont_righe

def main():
    file = lettura_file()
    statistica_parola = conta_parole(file)
    file_statistiche = open("es_002_statistiche.txt","w")
    file_statistiche.write(f"percentuale nome 'renzo' nel file: {statistica_parola*100}")
    file_statistiche.close()

if __name__ == "__main__":
    main()