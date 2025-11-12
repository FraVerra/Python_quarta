#stesso esericizio della password ma devo oscurare tutto tranne la prima lettera e l'ultima 

password = input("inserisci la password: ")

passwordBlanked = password[0] + "*" *(len(password) - 2) + password[-1]

print(f"password oscurata: {passwordBlanked}")