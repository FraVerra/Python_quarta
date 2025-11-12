#suddividere il codice in funzioni lo rende MODULARE, 
#modularità è una proprietà in cui il codice dev'essere suddiviso
#con moduli si intendono funzioni e ad esempio in java le classi

#permette di fare del codice leggibile, se contiene un errore è più facile da trovare testando le singole
#funzioni

#i tripli apici sarebbe un commendo che python si autogestisce, si chiama DOCSTRING  
#COSTANTE è una variabile globale, sono accessibile a qualunque funzione
#ATTENZIONE: sono accessibile a qualunque funzione soltanto in lettura però
COSTANTE = 3.14

def primaLetteraMaiuscola(stringa):
    ''' 
    la funzione restituisce stringa con la lettera iniziale maiuscola 
    '''
    s = stringa[0].upper() + stringa[1:].lower()
    return s #serve per ritornare, in questo caso ritorno la stringa

def media(lista):
    '''
    la funzione restituisce la media dei valori presenti in lista e il numero di elementi di lista
    NELLE FUNZIONI POSSO RESTITUIRE DUE O PIÙ VALORE 
    '''
    somma = 0
    n_lista = len(lista)
    for val in lista:
        somma = somma + val

    return somma/n_lista, n_lista

def main():
    #nome = input("inserisci una parola -> ")
    #print(primaLetteraMaiuscola(nome))
    voti = [4.5, 10, 8.25, 7 , 6]
    m, n = media(voti)
    print(f"la media è: {m}\til numero dei voti è: {n}")

if __name__ == "__main__":
    main()
