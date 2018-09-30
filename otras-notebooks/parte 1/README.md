# Modelo de regex para determinar los ambientes.
df["ambientes"]= df['description'].str.extract('(\d*|mono|\w*)\s*?amb\w*', expand=True)
