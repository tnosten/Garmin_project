import dlt
import os
from garminconnect import Garmin
from dotenv import load_dotenv
import duckdb

# Load environment variables
load_dotenv()

################# connect to  DuckDB
conn = duckdb.connect("./data/garmin_pipeline.duckdb")

# Run a simple query
df = conn.execute("SELECT * FROM garmin_data.activities").fetchdf()
print(df)


## drop table

# conn.execute("DROP SCHEMA IF EXISTS garmin_data CASCADE;")

conn.close()

