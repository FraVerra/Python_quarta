'''
Traduttore di parole
Dato un dizionario italiano-inglese e una frase in italiano, restituire la frase tradotta. Se
una parola non è nel dizionario, lasciarla invariata.
dizionario = {
"ciao": "hello",
"mondo": "world",
"casa": "house",
"gatto": "cat",
"cane": "dog",
"libro": "book",
"albero": "tree"
}
frase = "ciao mondo il gatto è in casa"
'''

def inserire():
    stringa = input("inserisci una stringa: ")
    return stringa

def diz():
    diz = {"ciao":"hello","mondo":"world","casa":"house","gatto":"cat","cane":"dog","libro":"book","albero":"tree"}
    return diz

def traduttore(stringa, diz):
    parole = []
    frase = []
    parole = stringa.split(" ")
    for dato in parole:
        if dato in diz:
            frase.append(diz[dato])
        else:
            frase.append(dato)
    return frase

def correttore(frase):
    frase_corretta = ""
    for dato in frase:
        frase_corretta = frase_corretta + f" {dato}"
    print(f"frase tradotta: {frase_corretta}")

def main():
    stringa = inserire()
    dizionario = diz()
    frase = traduttore(stringa, dizionario)
    correttore(frase)

if __name__ == "__main__":
    main()