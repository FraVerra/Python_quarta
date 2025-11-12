#NON SI POSSONO USARE I CICLI

#crea un programma in python che chiede all'utente il suo nome
#e lo stampa sempre con l'iniziale maiuscola

nome = input("inserisci il tuo nome: ")
nome = nome.lower()

nome_giusto = nome[0].upper() + nome[1:5]

print(nome_giusto)


