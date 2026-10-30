import pandas as pd
import time

rows = 100000

start_time = time.time()

df = pd.DataFrame({
    "customer_id": range(rows),
    "name": ["Test"] * rows,
    "age": [25] * rows
})

df.to_parquet(
    "data/incoming/performance.parquet",
    index=False
)

end_time = time.time()

print(
    f"{rows} rows generated in "
    f"{end_time - start_time:.2f} seconds"
)
