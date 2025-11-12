file = open("./nome_file","r")

riga = file.readlines()
for dati in riga:
    if(dati[0] == '#'){
        print(riga)
    }

file.close()