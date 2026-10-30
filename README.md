Objective of Schema Evolution Pipeline
Create pipeline to read multiple Parquet batches with compatible and incompatible schema changes. Detect schema drift, apply approved evolution rules and quarantine breaking changes.

Features
Ingesting parquet
Schema validation
Business validation process
Compatible schema evolution
Quarantine for breaking changes
Collecting metrics
Idempotent Processing .
Incoming Parquet Files Automated Testing Architecture | V Ingestion | V Schema Validation | | Valid Invalid | | V V Business Quarantine Validation | V Transform | V Publish | V Metrics

Run Commands Generate Sample Data

Run Pipeline 
python src/data_generator.py

python main.py

Run Tests

pytest 
Assumptions customer_id is primary key city and country are approved schema additions duplicate customer_id records are rejected
Improvements Coming Soon
DuckDB Analytical Engine:
Integration with Apache Spark
Airflow Schedule
Data Quality Dashboard

Data Set
The project employs programmatically generated synthetic datasets.

Examples of batches include:

Good recordkeeping
Compatible evolution of schema
Schema changes that break
Duplicated data
To test performance a bigger data set is generated (100,000 records).