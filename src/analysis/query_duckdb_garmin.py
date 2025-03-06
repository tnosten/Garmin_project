import dlt
import os
from garminconnect import Garmin
from dotenv import load_dotenv
import duckdb
import pandas as pd
import streamlit as st

# Load environment variables
load_dotenv()

################# connect to  DuckDB
conn = duckdb.connect("./data/garmin_pipeline.duckdb")

with duckdb.connect("./data/garmin_pipeline.duckdb") as conn:
    df = conn.execute("SELECT * FROM garmin_data.activities").fetchdf() # get all activities



#explore data
df.info()
df.to_csv("output.csv", index=False)  # Save without index


# fastest 1K

fastest_1k = conn.execute("""
    SELECT
        activity_name, 
        start_time_local AS datetime, 
        MAX(CAST(fastest_split_1000 AS float)/60) AS fastest_1k 
    FROM garmin_data.activities
    GROUP BY activity_name, datetime
    ORDER BY fastest_1k asc
    limit 1
""").fetchdf()

print(fastest_1k)

# fastest 1M


fastest_1mile = conn.execute("""
    SELECT
        activity_name, 
        start_time_local AS datetime, 
        MAX(CAST(fastest_split_1609 AS float)/60) AS fastest_1mile 
    FROM garmin_data.activities
    GROUP BY activity_name, datetime
    ORDER BY fastest_1mile asc
    limit 1
""").fetchdf()

print(fastest_1mile)



# fastest 5K

fastest_5k = conn.execute("""
    SELECT
        activity_name, 
        start_time_local AS datetime, 
        MAX(CAST(fastest_split_5000 AS float)/60) AS fastest_5k 
    FROM garmin_data.activities
    GROUP BY activity_name, datetime
    ORDER BY fastest_5k asc
    limit 1
""").fetchdf()

print(fastest_5k)



best_efforts = conn.execute("""
    WITH 
    five_k_best AS (
        SELECT 
            '5K' AS best_effort, 
            MIN(CAST(fastest_split_5000 AS float) / 60) AS time
        FROM garmin_data.activities
        LIMIT 1
    ),
    one_k_best AS (
        SELECT 
            '1K' AS best_effort, 
            MIN(CAST(fastest_split_1000 AS float) / 60) AS time
        FROM garmin_data.activities
        LIMIT 1
    ),
    one_mile_best AS (
        SELECT 
            '1 mile' AS best_effort, 
            MIN(CAST(fastest_split_1609 AS float) / 60) AS time
        FROM garmin_data.activities
        LIMIT 1
    ),
    Final as (
        Select * from five_k_best
        UNION
        Select * from one_k_best
        UNION
        Select * from one_mile_best
        )
    SELECT * FROM Final
                            
""").fetchdf()


print(best_efforts)

st.title("My DataFrame Viewer")
st.dataframe(best_efforts)  # Displays in Streamlit





## drop table

# conn.execute("DROP SCHEMA IF EXISTS garmin_data CASCADE;")

conn.close()

