def temp_media(dati):
    somma = 0
    cont = 0
    for valori in dati:
        somma += valori["temp"]
        cont += 1
    return somma/cont

def filtra_citta(dati, nome):
    variazioni = []
    for valori in dati:
        if valori["citta"] == nome:
            variazioni.append(valori["temp"])
    return variazioni

def temp_per_citta(dati):
    #restituisce dizionario, chiavi = città, valori = liste temp di quella città
    diz_nuovo = {}
    for valori in dati:
        lista = []
        if valori["citta"] not in diz_nuovo:
            lista.append(valori["temp"])
            diz_nuovo[valori["citta"]]=lista
        else:
            lista = diz_nuovo[valori["citta"]]
            lista.append(valori["temp"])
            diz_nuovo[valori["citta"]]=lista

    return diz_nuovo

def carica_regioni(nome_file):
    righe = nome_file.split("\n")
    diz = {}
    for dati in righe:
        parole = dati.split(";")
        diz[parole[0]]=parole[1]
    return diz

def main():
    dati = [
        {"citta":"Milano", "temp":12},
        {"citta":"Roma", "temp":18},
        {"citta":"Milano", "temp":14},
        {"citta":"Napoli", "temp":20},
        {"citta":"Roma", "temp":17},
        {"citta":"Napoli", "temp":22},
        {"citta":"Milano", "temp":10}
    ]
    media_valori = temp_media(dati)
    print(f"{media_valori:.2f}")
    variazioni = filtra_citta(dati, "Milano")
    print(f"le variazioni per la città di Milano sono: {variazioni}")
    diz_nuovo = temp_per_citta(dati)
    print(diz_nuovo)

    file = open("regioni.txt","r")
    contenuto_file = file.read()
    diz_regione = carica_regioni(contenuto_file)
    print(diz_regione)
    file.close()

if __name__ == "__main__":
    main()