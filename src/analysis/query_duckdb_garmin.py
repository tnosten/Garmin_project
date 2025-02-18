import dlt
import os
from garminconnect import Garmin
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

################# read from DuckDB
conn = duckdb.connect("garmin_pipeline.duckdb")

# Run a simple query
df = conn.execute("SELECT * FROM garmin_data.activities").fetchdf()
print(df)