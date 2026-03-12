import socket as so

SRV_ADDR = "192.168.50.100"
SRV_PORT = 44444

# prima di poter usare socket devo chiamare 
# socket e' estremamente generico qui chiedo ipv4 e tcp
s = so.socket(so.AF_INET, so.SOCK_STREAM)

# prima di usarlo lo devo configurare
# voglio chiedergli di configurarsi in ascolto
s.bind((SRV_ADDR, SRV_PORT))

# spiego quante connessioni puo' accettare
s.listen(1)

print("Server avviato, sono in attesa di connessione ...")
# Arrivati a questo punto quando do s.accept() attedera' che una connessione venga stabilita
# accept crea una tupla, la connessione stessa e delle informazioni
connection, address = s.accept()
# a questo punto il programma riprende
print("Connesso con:", address)
# avvio un ciclo infinito
while True:
    # mando un messaggio
    connection.sendall(b"shell#: ")
    # attendo la sua risposta per max 1024 caratteri
    data = connection.recv(1024)
    # se chiude la connessione chiudo il ciclo infinito
    if not data: break
    # stampo quello la domanda dell'utente
    print(data.decode("utf-8"))

# se esce dal ciclo chiudo la connessione, cosi' libero la porta
connection.close()


