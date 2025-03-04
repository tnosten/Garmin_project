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

# get all activities
df = conn.execute("SELECT * FROM garmin_data.activities").fetchdf() 

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



# Get the row with the highest "Split" values in seconds
fastest_1k = df.loc[df["fastest_split_1000"].idxmax()]
fastest_1mile = df.loc[df["fastest_split_1609"].idxmax()]
fastest_5k = df.loc[df["fastest_split_5000"].idxmax()]
print(fastest_1k)

df.head(max())
print(df)




st.dataframe(all_activities) #save to to a streamlit dataframe





## drop table

# conn.execute("DROP SCHEMA IF EXISTS garmin_data CASCADE;")

conn.close()

