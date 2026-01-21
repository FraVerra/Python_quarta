#Se la parola è "robot", scrivi a mano i passaggi per ottenere "tobor" usando un ciclo for.

a = input("inserisci una parola: ")

contrario = " "

cont = 0

for i in range(len(a)-1,-1, -1):

    contrario = contrario + a[i]

print(f"parola al contrario: {contrario}")


