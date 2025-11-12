ip = input("inserisci un indirizzo IP: ")
#.split è un metodo delle stringhe che suddivide una stringa cercando il carattere separatore passato
ottetti_str = ip.split(".")#è una lista
print(ottetti_str)

ottetti = []#lista vuota

for num in ottetti_str:
    ottetti.append(int(num))

print(ottetti)
print(bin(ottetti[0]))#python bin converte un numero intero a STRINGA binario con prefisso 0b