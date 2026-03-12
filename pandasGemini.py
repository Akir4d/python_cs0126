import pandas as pd
from google import genai
from google.genai import types
import os

# La nostra chiave non deve essere mai scritta nel codice
chiave = os.environ["GEMINI_API_KEY"]
# Instanzio un client genai e lo configuro con la chiave 
client = genai.Client(api_key=chiave)

# leggo il csv
df = pd.read_csv("auth.log.csv")

# Filtra solo per gli eventi falliti
eventi_falliti = df['message'].str.contains('Failed', case=False, na=False)
# Ottengo un elenco ordinato di eventi sospetti
sospetti = df[eventi_falliti].head(200)

# Printo 1 converto in stringa i dati
log_text = sospetti.to_string()

# Preparo il prompt per l'intelligenza arificiale
prompt = f"""
Analizza questi log e rispondi SOLO con JSON valido:
{{
  "anomalies": [
    {{
      "type": "brute_force",
      "src_ip": "...",
      "severity": "HIGH",
      "action": "Block IP"
    }}
  ]
}}

Log:
{log_text}
"""

# Interrogo l'inteligenza artificiale
response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=prompt
)

print(response.text)
