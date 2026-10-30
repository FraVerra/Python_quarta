#Chiedi una parola e una lettera.
#Stampa quante volte quella lettera compare nella parola.

parola = input("inserisci una parola: ")
car = input("inserisci un carattere: ")

cont  = 0

for i in range(len(parola)):

    if parola[i] == car:

        cont = cont + 1

if cont == 0:

    print(f"la lettera {car} non è mai presente nella parola")

else:

    print(f"la lettera {car} nella parola è presente: {cont} volte")