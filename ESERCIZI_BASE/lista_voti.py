#caricare 10 voti, stampare senza il 1 e ultimo, sostituire il 4 con un 10 e stampare i primi 3

lista = []

for i in range (10):

    a = int(input(f"inserisci il {i+1}^ numero della lista:"))
    lista.append(a)

print(lista[1:-1])
lista[3] = 10
print(lista[:4])


