def validate_business_rules(df):

    errors = []

    # Null customer_id
    null_ids = df["customer_id"].isnull().sum()

    if null_ids > 0:
        errors.append(
            f"Found {null_ids} null customer_id values"
        )

    # Duplicate customer_id
    duplicate_count = df.duplicated(
        subset=["customer_id"]
    ).sum()

    if duplicate_count > 0:
        errors.append(
            f"Found {duplicate_count} duplicate customer_id values"
        )

    # Age validation
    if "age" in df.columns:

        invalid_age = (df["age"] <= 0).sum()

        if invalid_age > 0:
            errors.append(
                f"Found {invalid_age} invalid age values"
            )

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }
