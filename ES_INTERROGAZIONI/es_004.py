lista = ["luca","mario","alice","giovanni"]
nMax = 0
nomeMax = ""

for nome in lista:
    n = len(nome)
    if n > nMax:
        nMax = n
        nomeMax = nome

print(f"nome più lungo: {nomeMax}")