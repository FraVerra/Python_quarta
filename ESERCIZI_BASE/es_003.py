#crea un programma che chieda all'utente un numero intero e stampa se il numero è divisibile per 2, 3 o 5
#usare operatore %!!!

n = int(input("inserisci un numero: "))

if(n % 2 == 0):

    print(f"il numero {n} è divisibile per 2!")

elif (n % 3) == 0:

    print(f"il numero {n} è divisibile per 3!")

elif (n % 5) == 0:

    print(f"il numero {n} è divisibile per 5!")

else:

    print(f"il numero {n} non è divisibile ne per 2 ne per 3 e nemmeno per 5")

