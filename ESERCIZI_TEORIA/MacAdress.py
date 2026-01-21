def main():

    file = open("./mac-vendors-export.csv","r")
    dati = file.readlines()
    macAdress = input("inserisci un MAC adress valido: ")
    file.close()

if __name__ == "__main__":
    main()
