lista=[1, 2, "ciao", [34,56], {"nome":"Pippo", "cognome": "Elkan"}]
print(lista[2])
print(lista[4])
lista.append("Non era una citazione")
print(lista)
lista.insert(3,"belli")
print(lista)

# rimuovere elementi metodo 1
lista.remove("ciao")
print(lista)
# rimuovere elementi metodo 2
del lista[0]
print(lista)
# rimovere ultimo elemento
lista.pop()
print(lista)

# sostituzione elemento
lista[1] = "Ciao belli!"
print(lista)

