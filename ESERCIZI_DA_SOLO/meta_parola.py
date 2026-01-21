#chiedere una parola e stampare solo la seconda meta

a = input("inserisci una parola: ")

dim = len(a)
meta = int(dim / 2)

print(a[meta:dim])
