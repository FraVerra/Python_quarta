import funzione1
import random

def main():
    voti = [random.randint(2,10) for i in range(10)]#una lista di 10 voti casuali
    print(f"voti: {voti}")
    m,n = funzione1.media(voti)
    print(m)

if __name__ == "__main__":
    main()