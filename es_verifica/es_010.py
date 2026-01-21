'''
Voto più frequente
Dato un dizionario che associa nomi di studenti ai loro voti (un voto per studente),
trovare quale voto compare più spesso.
studenti_voti = {
"Marco": 7,
"Sara": 8,
"Luca": 6,
"Elena": 8,
"Paolo": 7,
"Giulia": 8,
"Andrea": 6,
"Chiara": 7
}
'''

def dizionario():
    studenti_voti = {
    "Marco": 7,
    "Sara": 8,
    "Luca": 6,
    "Elena": 8,
    "Paolo": 7,
    "Giulia": 8,
    "Andrea": 6,
    "Chiara": 7
    }
    return studenti_voti

def controllo(diz):
    voto_maggiore = 0
    cont_voti = {}
    for dati in diz:
        if diz[dati] in cont_voti:
            cont_voti[diz[dati]] = cont_voti[diz[dati]]+1
        else:
            cont_voti[diz[dati]] = 1
    for i, dati in enumerate(cont_voti):
        if i == 0:
            voto_maggiore = dati
        else:
            if voto_maggiore < cont_voti[dati]:
                voto_maggiore = dati

    print(f"il voto con frequenza maggiore: {voto_maggiore}")

def main():
    diz = dizionario()
    controllo(diz)
if __name__ == "__main__":
    main()