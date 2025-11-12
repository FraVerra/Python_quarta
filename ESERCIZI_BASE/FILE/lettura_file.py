file = open("./dati.csv","r") #questo è un oggetto file

righe = file.readlines() #serve per leggere le righe, avessi mesos file.readline() al singolare legge 1 riga
                       #è una lista 
file.close() #mi raccomando sempre chiudere il file!

titoli1, titolo2, titolo3 = righe[0][:-1].split(",")#stampo omettendo la \n
print(titoli1)
print(titolo2)
print(titolo3)