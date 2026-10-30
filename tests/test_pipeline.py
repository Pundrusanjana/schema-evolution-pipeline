import sys
import os

sys.path.append(
    os.path.abspath("src")
)

import pandas as pd

from business_validator import validate_business_rules


def test_valid_data():

    df = pd.DataFrame({
        "customer_id": [1, 2],
        "name": ["John", "Mike"],
        "age": [25, 30]
    })

    result = validate_business_rules(df)

    assert result["valid"] is True


def test_duplicate_customer():

    df = pd.DataFrame({
        "customer_id": [1, 1],
        "name": ["John", "John"],
        "age": [25, 25]
    })

    result = validate_business_rules(df)

    assert result["valid"] is False


def test_null_customer_id():

    df = pd.DataFrame({
        "customer_id": [1, None],
        "name": ["John", "Mike"],
        "age": [25, 30]
    })

    result = validate_business_rules(df)

    assert result["valid"] is False