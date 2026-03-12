import socket as so

target = input("Indirizzo IP da scansire: ")
# ho bisogno di un range di porte da scansire
prtran = input("Inserisci un range di porte (es 5-200): ")

# "scoppiare" highport e la lowport
lowport = int(prtran.split("-")[0])
higport = int(prtran.split("-")[1])
# preparo una lista vuota
portechiuse = []
# informo l'utente
print(f"Sto scansendo {target} dalla porta {lowport} alla porta {higport}")

for port in range(lowport, higport+1):
    # configuriamo socket
    s = so.socket(so.AF_INET, so.SOCK_STREAM)
    # abbiamo bisogno di una connessione "mordi e fuggi"
    status = s.connect_ex((target, port))
    # a questo punto se lo stato e' 0 la connessione ha avuto successo!
    if(status == 0):
        print(f"*** Porta {port} - Aperta ***")
    else:
        portechiuse.append(port)
        #print(f"Porta {port} - Chiusa")
    s.close()

# print("porte chiuse: ", portechiuse)
print(f"individuate {len(portechiuse)} porte chiuse")


