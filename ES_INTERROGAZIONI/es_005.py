lista = ["lolli", "gallina","cane","pterodattilo"]
k = 0

for nome in lista:
    lista[k] = nome.upper()
    print(f"nome maiuscolo: {lista[k]}")
    k = k+1
