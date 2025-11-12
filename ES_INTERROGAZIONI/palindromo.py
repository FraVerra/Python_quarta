a = input("inserisci una frase: ")
a = a.lower()

if a == a[::-1]:
    print("la stringa è la palindroma")
else:
    print("la stringa non è palindroma")
