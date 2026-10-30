Column	Data Type	Required	Description
customer_id	int64	Yes	Customer primary key
name	string	Yes	Customer name
age	int64	No	Customer age
city	string	No	Allowed schema evolution column
run_id	string	Yes	Pipeline run identifier
source_file	string	Yes	Input parquet file
processed_timestamp	string	Yes	Processing timestamp