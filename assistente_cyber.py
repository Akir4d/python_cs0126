from google import genai
from google.genai import types
import os

# La nostra chiave non deve essere mai scritta nel codice
chiave = os.environ["GEMINI_API_KEY"]
# Instanzio un client genai e lo configuro con la chiave 
client = genai.Client(api_key=chiave)

config = types.GenerateContentConfig(
    temperature=0.2,
    max_output_tokens=1024,
    system_instruction="""
    Sei un tutor di sicurezza informatica per studenti principianti.
    Spiega i concetti in modo semplice, con esempi pratici.
    Se non sai qualcosa, dillo chiaramente.
    """
)

while True:
    # Qui faccio una domanda
    domanda=input("Tu: ")

    # mi occorre una via d'uscita!
    if domanda.lower().strip() == "esci":
        print("Arrivederci!")
        break

    # Genera risposta
    response = client.models.generate_content(
        model="gemini-2.5-flash", # chiedo a google di usare il modello veloce
        contents=domanda, # faccio una domanda al modello
        config=config
    )

    # Stampa output
    print(f"AI: {response.text}\n")
