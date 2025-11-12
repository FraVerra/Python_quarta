ip = input("inserisci un indirizzo IP valido -> ")

ottetti_str  = ip.split(".")
ottettiCorretti = []#lista vuota

for num in ottetti_str:
    ottettiCorretti.append(int(num))
    binario = bin(ottettiCorretti[-1])
    print(binario[2::], end=".")


