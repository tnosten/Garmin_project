import dlt
import duckdb
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up dlt pipeline
pipeline = dlt.pipeline(
    pipeline_name="garmin_pipeline",
    destination="duckdb",
    dataset_name="garmin_data"
)

# Example function to load data
def load_example_data():
    data = [
        {"activity": "Running", "distance_km": 5.2, "duration_min": 30},
        {"activity": "Cycling", "distance_km": 15.5, "duration_min": 45}
    ]

    # Load data into DuckDB
    pipeline.run(data, table_name="activities")

if __name__ == "__main__":
    load_example_data()
    print("Data loaded into DuckDB!")



################# read from DuckDB
conn = duckdb.connect("garmin_pipeline.duckdb")

# Run a simple query
df = conn.execute("SELECT * FROM garmin_data.activities").fetchdf()
print(df)
