#chiedere all'utente due numeri e il tipo di calcolo che vuole effettuare

primo = int(input("inserisci il primo numero: "))
secondo = int(input("inserisci il secondo numero: "))

print("0 = somma, 1 = sottrazione, 2 = moltiplicazione, 3 = divisione")
calcolo = int(input("fai la tua scelta: "))

if calcolo == 0:

    somma = primo + secondo
    print(f"la somma tra {primo} e {secondo} da come risultato {somma}")

elif calcolo == 1:

    sott = primo - secondo
    print(f"la sottrazione tra {primo} e {secondo} da come risultato {sott}")

elif calcolo == 2:

    molt = primo * secondo
    print(f"la moltiplicazione tra {primo} e {secondo} da come risultato {molt}")

elif calcolo == 3:

    if secondo == 0:

        print("non è possibile dividere per 0...")

    elif (primo == 0 & secondo != 0):

        print("risulato uguale a 0")

    else:

        div = primo / secondo
        print(f"la divisione tra {primo} e {secondo} da come risultato {div}")


