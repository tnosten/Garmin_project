import dlt
import os
from garminconnect import Garmin
from dotenv import load_dotenv
from dlt.sources.rest_api import RESTAPIConfig

# Load environment variables
load_dotenv()

GARMIN_USERNAME = os.getenv("GARMIN_USERNAME")
GARMIN_PASSWORD = os.getenv("GARMIN_PASSWORD")

# Authenticate with Garmin Connect
def authenticate_garmin():
    try:
        garmin = Garmin(GARMIN_USERNAME, GARMIN_PASSWORD)
        garmin.login()
        return garmin
    except Exception as e:
        print(f"Garmin authentication failed: {e}")
        return None

# Function to fetch Garmin activities
def fetch_garmin_activities(garmin, limit=1000):
    try:
        return garmin.get_activities(0, limit)  # Fetches latest 'limit' activities
    except Exception as e:
        print(f"Failed to fetch activities: {e}")
        return []

# Create the dlt pipeline
def load_garmin_activities():
    pipeline = dlt.pipeline(
        pipeline_name="garmin_pipeline",
        destination=dlt.destinations.duckdb("./data/garmin_pipeline.duckdb"),
        dataset_name="garmin_data"
    )

    garmin = authenticate_garmin()
    if not garmin:
        return

    # Fetch data from Garmin
    activities = fetch_garmin_activities(garmin)

    # Load data into DuckDB
    load_info = pipeline.run(
        activities, 
        table_name="activities",
        write_disposition="merge",  # Avoid duplicates
        primary_key="activityId",   # Garmin's unique identifier for activities
        )
    print(load_info)

if __name__ == "__main__":
    load_garmin_activities()





# import dlt

# pipeline = dlt.pipeline(
#     pipeline_name="garmin_pipeline",
#     destination="duckdb"
# )

# print(pipeline.destination.config)



# import dlt

# pipeline = dlt.pipeline(
#     pipeline_name="garmin_pipeline",
#     destination="duckdb"
# )

# print(vars(pipeline.config))  # Check all loaded configs
