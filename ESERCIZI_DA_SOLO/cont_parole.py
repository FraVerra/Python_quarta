#Chiedi una frase e stampa quante parole contiene.

n = input("inserisci una frase: ")

cont = 1

for i in range(len(n)):

    if n[i] == ' ':

        cont = cont + 1

print(f"nella frase sono presenti: {cont} parole")