print("Premi A per inserire.")
print("Premi B per modificare.")
print("Premi C per volare")

tasto = input("-> ")
tasto = tasto.upper()#adesso qualunque cosa metta l'utente diventa maiuscolo
#.lower() trasforma tutto in minuscolo 

if(tasto == "A"):

    print("utente vuole inserire...")

elif tasto == "B":

    print("utente vuole modificare...")

elif tasto == "C":

        print("utente vuole volareeeee")

else:

    print("tasto non valido!!!")
