import re

testo = "Utente 1: 192.168.45.34, Utente 2: 192.168.45.22"
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
cerca = re.findall(pattern, testo)
primo = re.search(pattern, testo)
print(cerca)
print(primo)