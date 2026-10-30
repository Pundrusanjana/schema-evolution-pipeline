import uuid
from datetime import datetime


def transform_data(df, source_file):

    df["run_id"] = str(uuid.uuid4())

    df["source_file"] = source_file

    df["processed_timestamp"] = (
        datetime.now()
        .isoformat()
    )

    return df