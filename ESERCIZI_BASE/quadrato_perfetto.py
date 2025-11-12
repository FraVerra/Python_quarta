#la somma dei numeri dispari è sempre un quadrato perfetto

import math

n = int(input("quanti numeri dispari vuoi: "))
somma = 0

if n < 0:

    print("numero non valido")

elif (n == 0):

    print("nessun numero")

elif (n > 0):

    for i in range(1, n*2+1, 2):

            somma = somma + i

    radice_intera = math.isqrt(somma)
    print(f"la somma è: {somma}, Quadrato perfetto: {radice_intera** 2 == somma}")#cosi lui stampa true o false!
    