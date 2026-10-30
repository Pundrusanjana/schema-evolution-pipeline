import pandas as pd
import os

os.makedirs("data/incoming", exist_ok=True)

# Batch 1 - Normal Data
batch1 = pd.DataFrame({
    "customer_id": [1, 2, 3],
    "name": ["John", "Mike", "Sarah"],
    "age": [25, 30, 28]
})

# Batch 2 - Compatible Schema Change
batch2 = pd.DataFrame({
    "customer_id": [4, 5, 6],
    "name": ["Tom", "Anna", "David"],
    "age": [35, 26, 40],
    "city": ["NY", "LA", "Chicago"]
})

# Batch 3 - Breaking Change
batch3 = pd.DataFrame({
    "customer_id": [7, 8],
    "full_name": ["Robert Smith", "Jane Doe"],
    "age": [29, 31]
})

# Batch 4 - Duplicate Records
batch4 = pd.DataFrame({
    "customer_id": [9, 9],
    "name": ["Chris", "Chris"],
    "age": [22, 22]
})

batch1.to_parquet("data/incoming/batch1.parquet", index=False)
batch2.to_parquet("data/incoming/batch2.parquet", index=False)
batch3.to_parquet("data/incoming/batch3.parquet", index=False)
batch4.to_parquet("data/incoming/batch4.parquet", index=False)

print("All test batches created successfully!")