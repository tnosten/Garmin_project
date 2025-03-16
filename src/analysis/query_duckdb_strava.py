from dotenv import load_dotenv
import duckdb

# Load environment variables
load_dotenv()

################# connect to  DuckDB
conn = duckdb.connect("./data/strava_pipeline.duckdb")

# Run a simple query
# df = conn.execute("SELECT * FROM strava_data.activities").fetchdf()

df = conn.execute("SELECT * FROM information_schema.tables").fetchdf()
print(df)


## drop table

# conn.execute("DROP SCHEMA IF EXISTS garmin_data CASCADE;")

conn.close()

