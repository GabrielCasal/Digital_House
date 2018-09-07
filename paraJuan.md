# Digital_House
df["ambientes"]= df['description'].str.extract('(\d*|mono|\w*)\s*?amb\w*', expand=True)
