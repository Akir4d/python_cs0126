def menu():
    while True:
        print("Menu'")
        print("1 - Fai il quadrato")
        print("2 - Fai il rettangolo")
        print("3 - Fai i cerchio")
        print("4 - Esci")
        scelta = input("Scegli: ")
        try:
            scelta = int(scelta)
        except:
            scelta = 0
        if scelta > 4: 
            scelta = 0
        if (scelta != 0): break    
    return scelta
    
scelta = menu()
print(scelta)