'''
Conta righe e parole
Leggere un file di testo e stampare: numero di righe, numero di parole, numero di
caratteri (esclusi gli spazi).
File testo.txt:
Python è un linguaggio di programmazione.
È semplice da imparare e molto potente.
Viene usato in molti ambiti diversi.
'''

def contatore(file):
    contenuto = file.read()
    righe = (contenuto.split("\n"))
    parole = (contenuto.split(" "))
    lettere = 0
    for dati in contenuto:
        if dati != " " or dati != "\n" or dati != ".":
            lettere += 1
    print(f"righe: {righe}   parole: {parole}   lettere: {lettere}")

def main():
    file = open("file.txt","r")
    contatore(file)
    file.close()

if __name__ == "__main__":
    main()