import pandas as pd

# leggo il csv
df = pd.read_csv("auth.log.csv")

# Filtra solo per gli eventi falliti
eventi_falliti = df['message'].str.contains('Failed', case=False, na=False)
# Ottengo un elenco ordinato di eventi falliti
failed = df[eventi_falliti]

# Raggruppo per IP
by_ip = failed.groupby('src_ip').size()

# I top 10 attaccanti
top_attackers = by_ip.nlargest(10)
print(top_attackers)