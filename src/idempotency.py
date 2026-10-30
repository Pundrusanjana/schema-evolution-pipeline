import os
import csv


METADATA_FILE = (
    "data/metadata/processed_files.csv"
)


def is_processed(file_name):

    if not os.path.exists(METADATA_FILE):
        return False

    with open(
            METADATA_FILE,
            mode="r") as file:

        reader = csv.reader(file)

        for row in reader:

            if len(row) > 0:

                if row[0] == file_name:
                    return True

    return False


def mark_processed(file_name):

    file_exists = os.path.exists(
        METADATA_FILE
    )

    with open(
            METADATA_FILE,
            mode="a",
            newline=""
    ) as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow(
                ["file_name"]
            )

        writer.writerow(
            [file_name]
        )