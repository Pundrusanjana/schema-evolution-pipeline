import pandas as pd

df = pd.read_parquet(
    "data/incoming/batch1.parquet"
)

print(df)
