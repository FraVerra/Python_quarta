#scrivi un programma che calcoli quanti sono i quadrati perfetti minori di 200

import math

continua = True
cont = 0
somma = 0

for i in range(1, continua == True, 1):
    for k in range(1, i*2+1, 2):

        somma = somma + k
        radiceIntera = math.isqrt(somma)

        if (radiceIntera*2 != somma):

            continua = False

        else:

            cont = cont + 1

    if (somma < 200):

        continua == True

print(f"il numero dei quadrati perfetti minori di 200 sono: {cont}")