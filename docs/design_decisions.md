Design Decisions

Why use Pandas?
We chose pandas because it’s lightweight, easy to run locally, and fits our project scope.

Why Parquet Format?
Parquet is a columnar storage format that stores schema information and provides efficient storage and retrieval . It is industry standard .

Why Isolation? 
Invalid files are quarantined and not deleted. This enables the investigation and tracing of data quality issues.

Why Idempotency?
Idempotency ensures that duplicates are not processed, and reruns cause no issues.

Compromises
We opted for Pandas over Apache Spark to reduce the setup complexity and keep the solution easy to review and run locally.

Limitations :
Running on a single machine
No scheduling of workflow
No distributed processing.
Future Enhancements
Integration with Apache Spark
Apache Airflow Scheduling.
DuckDB analytical layer
Dashboard of data quality