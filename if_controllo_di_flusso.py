# int converte una varibile in intero, con utile con input
x=int(input("Dammi il valore di x: "))
y=int(input("Dammi il valore di y: "))

print("la somma di",x, "e di", y, "e'", x+y)

if x<y:
    print("x e' minore di y")
elif (x == y): # le parantesi sono opzionale per un singolo controllo
    print("x e' uguale a y")
else:
    print("x e' maggiore di y")