import yaml


def load_schema_config():
    """
    Load schema configuration from YAML file
    """

    with open("config/schema.yml", "r") as file:
        return yaml.safe_load(file)


def validate_schema(df):
    """
    Validate incoming dataframe schema
    """

    config = load_schema_config()

    expected_schema = config["expected_schema"]
    required_columns = config["required_columns"]
    allowed_new_columns = config["allowed_new_columns"]

    errors = []

    # Check required columns
    for column in required_columns:
        if column not in df.columns:
            errors.append(
                f"Missing required column: {column}"
            )

    # Check for unexpected columns
    for column in df.columns:

        if column not in expected_schema:

            if column not in allowed_new_columns:
                errors.append(
                    f"Unexpected column: {column}"
                )

    # Check datatype compatibility
    for column, expected_type in expected_schema.items():

        if column in df.columns:

            actual_type = str(df[column].dtype)

            if actual_type != expected_type:

                errors.append(
                    f"{column}: expected {expected_type}, found {actual_type}"
                )

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }