import http.client

host = input("Inserire host/IP del sistema target: ")
port = input("Inserire la porta del target (default: 80): ")

# imposto la porta 
if port == "": 
    port = 80

try:
    # configuro e instanzio (creo) la nuova connessione 
    conn = http.client.HTTPConnection(host, port)
    # Dopo la connessione invio al server i comandi
    conn.request("OPTIONS", "/")
    # gestiamo la risposta (qui si mette in pausa e invia la richesta configurata)
    response = conn.getresponse()
    # qui non sto chiedendo i verbi ma sto chidendo lo stato
    print("I metodi abilitati sono:", response.status)
    conn.close()
except ConnectionRefusedError:
    print("Connessione fallita")
except:
    print("Errore")
