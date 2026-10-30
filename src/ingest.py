import pandas as pd

def read_parquet(file_path):
    """
    Read a parquet file and return a dataframe
    """

    try:
        df = pd.read_parquet(file_path)
        return df

    except Exception as e:
        print(f"Error reading file: {e}")
        return None