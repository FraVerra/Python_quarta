#facciamo una funzioncina semplice che prende una stringa e la oscura tutta tranne il primo carattere

def oscuraPassword(s):
    len = len(s)
    parolaOscurata = s[0] + (len-1)*'*'
    return parolaOscurata

def main():
    lista = ["ciao","unoduetre"]
    listaOscurata = []
    parolaOscurata = ""
    cont = 0
    for parola in lista:
        parolaCoperta = parolaOscurata(parola)
        listaOscurata[cont] = parolaOscurata
        print(parolaOscurata)
    

if __name__ == '__main__':
    main()
