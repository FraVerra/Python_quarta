'''
Scrivi un programma che legge il file dati.csv contenente nome;cognome;età, 
stampa solo i maggiorenni, calcola l’età media e salva in maggiorenni.txt 
i nomi e cognomi dei maggiorenni.
'''

def lettura_file():
    datas = []
    file = open("es_001.csv","r")
    datas = file.readlines()
    file.close()
    return datas

def eta_media(dati_file):
    somma = 0
    cont = 0
    for campi in dati_file:
        dati = campi[0:-1].split(",")
        somma+=int(dati[-1])
        cont+=1
    return somma/cont

def stampa_maggiorenni(file):
    maggiorenni = open("es_001_maggiorenni.txt","w")
    for campi in file:
        dati = campi[0:-1].split(",")
        if(int(dati[-1]) >= 18):
            maggiorenni.write(f"{dati[0]} {dati[1]} {dati[-1]}\n")
    maggiorenni.close()

def main():
    file = lettura_file()
    media = eta_media(file)
    print(f"media delle età: {media}")
    stampa_maggiorenni(file)

if __name__ == "__main__":
    main()