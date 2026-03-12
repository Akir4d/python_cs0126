from google import genai
from google.genai import types
import os

# La nostra chiave non deve essere mai scritta nel codice
chiave = os.environ["GEMINI_API_KEY"]
# Instanzio un client genai e lo configuro con la chiave 
client = genai.Client(api_key=chiave)

config = types.GenerateContentConfig(
    temperature=0.9,
    max_output_tokens=1024,
    system_instruction="""
    Sei un assistete amichevole per studenti di programmazione.
    Rispondi in modo semplice e chiaro.
    Usa esempi pratici quando possibile
    """
)


# Genera risposta
response = client.models.generate_content(
    model="gemini-2.5-flash", # chiedo a google di usare il modello veloce
    contents="Ciao! Chi sei?", # faccio una domanda al modello
    config=config
)

# Stampa output
print(response.text)
