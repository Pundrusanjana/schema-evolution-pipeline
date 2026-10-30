import os
import uuid

from ingest import read_parquet
from schema_validator import validate_schema
from business_validator import validate_business_rules
from quarantine import quarantine_file
from transformer import transform_data
from publisher import publish_data
from metrics import save_metrics
from idempotency import (
    is_processed,
    mark_processed
)

INPUT_FOLDER = "data/incoming"

print("Main.py loaded")


def run_pipeline():

    files = [
        f for f in os.listdir(INPUT_FOLDER)
        if f.endswith(".parquet")
    ]

    print("Files Found:", files)

    for file_name in files:

        print("\n" + "=" * 50)
        print(f"Processing: {file_name}")

        # Idempotency
        if is_processed(file_name):

            print(
                f"Skipping already processed file: {file_name}"
            )

            continue

        run_id = str(uuid.uuid4())

        file_path = os.path.join(
            INPUT_FOLDER,
            file_name
        )

        # Read File
        df = read_parquet(file_path)

        if df is None:
            continue

        input_rows = len(df)

        # Schema Validation
        schema_result = validate_schema(df)

        if not schema_result["valid"]:

            quarantine_file(
                file_path,
                schema_result["errors"]
            )

            save_metrics(
                run_id,
                input_rows,
                0,
                input_rows,
                "SCHEMA_FAILED"
            )

            print(
                "Schema validation failed"
            )

            continue

        # Business Validation
        business_result = validate_business_rules(df)

        if not business_result["valid"]:

            quarantine_file(
                file_path,
                business_result["errors"]
            )

            save_metrics(
                run_id,
                input_rows,
                0,
                input_rows,
                "BUSINESS_FAILED"
            )

            print(
                "Business validation failed"
            )

            continue

        # Transform
        transformed_df = transform_data(
            df,
            file_name
        )

        # Publish
        publish_data(
            transformed_df,
            file_name
        )

        # Mark Processed
        mark_processed(file_name)

        output_rows = len(
            transformed_df
        )

        # Metrics
        save_metrics(
            run_id,
            input_rows,
            output_rows,
            0,
            "SUCCESS"
        )

        print(
            f"Completed: {file_name}"
        )


if __name__ == "__main__":
    run_pipeline()

     