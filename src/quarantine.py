import os
import shutil
import json


def quarantine_file(file_path, reason):

    # Create quarantine directory
    os.makedirs(
        "data/quarantine",
        exist_ok=True
    )

    file_name = os.path.basename(file_path)

    destination = os.path.join(
        "data/quarantine",
        file_name
    )

    # Move bad file
    shutil.copy(
        file_path,
        destination
    )

    # Save rejection reason
    reason_file = os.path.join(
        "data/quarantine",
        f"{file_name}.json"
    )

    with open(reason_file, "w") as f:
        json.dump(
            {"file": file_name,
             "reason": reason},
            f,
            indent=4
        )

    print(
        f"File quarantined: {file_name}"
    )