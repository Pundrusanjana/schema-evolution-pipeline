import csv
import os


def save_metrics(
        run_id,
        input_rows,
        output_rows,
        rejected_rows,
        status):

    os.makedirs(
        "data/metadata",
        exist_ok=True
    )

    metrics_file = (
        "data/metadata/pipeline_runs.csv"
    )

    file_exists = os.path.isfile(
        metrics_file
    )

    with open(
            metrics_file,
            mode="a",
            newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "run_id",
                "input_rows",
                "output_rows",
                "rejected_rows",
                "status"
            ])

        writer.writerow([
            run_id,
            input_rows,
            output_rows,
            rejected_rows,
            status
        ])