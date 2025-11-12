#in python abbiamo le collezioni, tra le collezioni abbiamo:
#liste, tuple,dizionari,set.

#vediamo le liste

#creare una lista
l = [3, 3.14, 10, "ciao", True]

#per accedere agli elementi vigono le stesse regole
#di INDICIZZAZIONE e SLICING delle stringhe

print(f"l'ultimo elemento della lista è: {l[-1]}")
print(l)
print(f"tutta la lista senza il primo e ultimo elemento è: {l[1:-1]}")

#aggiunta di un elemento
l.append("NUOVO")#non restituisce nulla ma modifica l!

l.pop()#va a rimuovere l'ultimo elemento della lista
l.pop()

print(l)