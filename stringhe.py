# posso scriive le stringhe in diversi modi
# doppi apici
nome="Gianpietro"
# apice singolo
altro_nome='Gianpeter'
# piu' apici serve per poter andare a capo, cosa non permessa con gli apici "" e ''
lista_spesa="""
Cibo,
Carta,
detersivo,
bicarbonato"""
lista_armi="""
fionda,
rametto,
caramelle gommose,
padelle"""

# stramente in python iniziere una riga con una stringa senza assegnarla
"Questo e' un commento in effetti"

"""
Anche questo e'
un commento in effetti
"""
# quando definisco una stringa in python sto in effetti definendo un oggetto
saluto="Hello, World"
saluto2=" Questo e' python"
print(saluto.split(',')) # questo stampa un lista ['Hello', ' World']
print(saluto.upper()) # questo stampa in maiuscolo
print(saluto+saluto2) # Hello, World Questo e' python
