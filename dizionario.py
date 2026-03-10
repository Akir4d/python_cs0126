persona={"nome": "Francesco", "cognome": "Stabile" , "eta": 46}

print(persona["nome"])
print(persona["cognome"])
print(persona["eta"])

persona["eta"]=36

print(persona)

# aggiungi elementi
persona["citta"]="Roma"
persona["email"]="nessuno@niente.org"
print(persona)

# rimuovere elemento
del persona["email"]
print(persona)

persona.pop("citta")
print(persona)

# solo valori
print(persona.values())

# solo le chiavi
print(persona.keys())

for key in persona.keys():
    print(key, '->', persona[key])

#  versione scolastica
for item in persona.items():
    key, value = item # destrutturazione dato, item e' tupla o lista gli elementi si possono destrutturare
    print(key, '->', value)

# compatta
for key, value in persona.items(): print(key, '->', value)
