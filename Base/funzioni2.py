variabile = 20

def mia_funzione():
    global variabile
    variabile=10
    print(variabile)

mia_funzione()
print(variabile)