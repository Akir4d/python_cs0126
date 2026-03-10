def saluta(nome):
    print(f"Ciao, {nome}! Come stai!")

def somma(num, den):
    try:
        num = int(num)
    except:
        return 0
    
    try:
        den = int(den)
    except:
        return 0
    
    return num + den

if __name__ == "__main__":
    n=input("primo numero: ")
    d=input("secondo numero: ")
    print(somma(n,d))

    result=somma(10, 30)
    print(result)

    nome = input("Come ti chiami? ")
    saluta(nome)