#modificare il codice sotto per:
# -stampare la media di ognuno
# -stampare il numero di voti per ognuno
# -stampare il massimo e il voto minimo


def main():
    lista_nomi = ["alice","sanPietro","giovanni","piero"]
    lista_voti = [[6,10,10],[4,3,5],[5,3,4,2,5,4], [0, 0]]

    #voglio stampare il voto a fianco di ogni nome

    for nome, voti in zip(lista_nomi, lista_voti):
        print(f"nome: {nome} - voti presi: {voti}")
        minimo = 10
        massimo = 0
        media = 0
        for voto in voti:
            media = media + voto
            if(massimo <= voto):
                massimo = voto
            if(minimo >= voto):
                minimo = voto
        media = media / len(voti)
        print(f"la media dei voti di {nome} è: {media}")
        print(f"voto massimo: {massimo}\tvoto minimo: {minimo}")

if __name__ == "__main__":#questo è "dunder" DOPPIO UNDERSCORE

    main()

#zip permette di ciclare il parallelo su due o piu liste