import pandas as pd
df = pd.read_parquet("Dados_Artistas.parquet")
pd.set_option('display.max_rows', None)


df.head(5)

df["Artist"].unique()

df['Artist'].nunique()

df['Artist'].value_counts().head(10)

df.sort_values(by="Views", ascending=False).head(5)["Track", "Artist"]

df.sort_values(by="Stream", ascending=False).head(5)["Artist", "Stream"]

df.to_parquet('Dados_Artistas.parquet', index=False)