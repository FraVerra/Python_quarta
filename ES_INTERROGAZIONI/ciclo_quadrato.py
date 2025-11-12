a = int(input("inserisci un numero: "))

if a >= 0:

    for i in range(a+1):

        q = i * i
        print(q, end=" ")

else:

    print("numero negativo!")