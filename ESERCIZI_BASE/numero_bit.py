#chiedere all'utente un numero di bit
#chiedere all'utente un numero binario gestito come stringa
#se la lunghezza del numero binario è minore del numero di bit, aggiungiamo a sinistra tanti 0
#quanto basti per raggiungere il numero di bit

n_bit = int(input("insersci un numero di bit: "))
n_binario = input("inserisci un numero binario: ")
dim_n_binario = len(n_binario)

if(dim_n_binario < n_bit):

    print("ERRORE")

else:

    for i in n_bit:

        n_binario = "0" + n_binario

print(n_binario)