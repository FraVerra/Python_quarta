macAdress = input("inserisci un mac adress: ")
macVendorName = ""

file = open("./mac-vendors-export.csv","r")
righe = file.readlines()
i = 0
trovato = False
for dati in righe:
    parts =  righe[i].split(",")
    macPrefix = parts[0]
    vendorName = parts[1]
    if macPrefix == macAdress[0:8]:
        macVendorName = vendorName
        trovato = True
    else:
        i = i+1

if trovato:
    print(f"produttore mac adress fornito: {macVendorName}")
else:
    print("mac adress non trovato")
file.close()