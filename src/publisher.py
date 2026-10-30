import os


def publish_data(df, file_name):

    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    output_path = (
        f"data/processed/{file_name}"
    )

    df.to_parquet(
        output_path,
        index=False
    )

    print(
        f"Published: {output_path}"
    )