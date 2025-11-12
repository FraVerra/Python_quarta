#il main in python non è obbligatorio, PYTHON E' LA VOCE DELLA LIBERTAAAAAAAAAA'(apostrofo)

def main():
    lista = ["alice","lucaLuchino","giovanni","marioMaria"]
    nome_max = None
    len_max = 0
    for nome in lista:
        if len(nome)>len_max:
            nome_max = nome
            len_max = len(nome)
    print(nome_max)

def main():
    lista = ["alice","lucaLuchino","giovanni","marioMaria"]

    for i, nome in enumerate(lista):
        print(f"{i} - {nome}")

if __name__ == "__main__":#questo è "dunder" DOPPIO UNDERSCORE
    print(__name__)
    main()

#questa if è falsa solo se noi ad esempio importiamo questo programma dentro un altro programma
