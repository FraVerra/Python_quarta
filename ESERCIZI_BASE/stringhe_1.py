#in python possiamo delimitare con "" oppure ''

stringa = "Ciao mondo"
print(stringa)

#esempio di indicizzazione della stringa, dato un indice lui va a estrarre il carattere
print(f"l'ultimo carattere della stringa è:\t {stringa[-1]}")

#esempio di slicing delle stringhe, tiriamo dalle stringhe delle sotto stringhe
print(f"la sotto stringa 2-5 è:\t{stringa[2:5]}.")#cosi mi va a stampare le lettere da A a O, mi prendi tutti i caratteri da quello in posizione 2(incluso) a quello posizione 5(escluso)
#quindi mi va a prendere i caratteri 2,3,4 solo questo QUI 

#assegnazione multipla
nome, cognome = "Mario", "Rossi"

x = nome + " " + cognome #le due stringhe vengono concatenate tra loro (senza gli spazi tra essi)
#mettendo gli apici posso andare a scrivere con degli spazi
print(x)

#cocncatenazione di una stringa con se stessa per più volte
y = (nome + " ")* 5
print(y)