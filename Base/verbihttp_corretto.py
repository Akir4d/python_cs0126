import http.client

host = input("Inserire host/IP del sistema target: ")
path = input("Inserire path: ")
port = input("Inserire la porta del target (default: 80): ")

# imposto la porta 
if port == "": 
    port = 80

try:
    # configuro e instanzio (creo) la nuova connessione 
    conn = http.client.HTTPConnection(host, port)
    # Dopo la connessione invio al server i comandi
    conn.request("OPTIONS", path)
    # gestiamo la risposta (qui si mette in pausa e invia la richesta configurata)
    response = conn.getresponse()
    # qui chiedo tutti gli headers Abilitare per debug
    # print("Headers ricevuti:", response.getheaders())
    # qui prendo gli headers se disponibili
    verbi = response.getheader('Allow')
    if verbi:
        print("I verbi sono: ", verbi)
    else:
        print("non ho trovato verbi")
    
    conn.close()
except ConnectionRefusedError:
    print("Connessione fallita")
except:
    print("Errore")
