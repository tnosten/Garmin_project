
from garminconnect import Garmin
from dotenv import load_dotenv
import duckdb
import pandas as pd
import streamlit as st

# Load environment variables
load_dotenv()

################# connect to  DuckDB

with duckdb.connect("./data/garmin_pipeline.duckdb") as conn:
    df = conn.execute("SELECT * FROM garmin_data.activities").fetchdf() # get all activities



    #explore data
    df.info()
    df.to_csv("output.csv", index=False)  # Save without index


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

    st.title("My Garmin Activities")
    st.dataframe(best_efforts)  # Displays in Streamlit

    ## Create a sample DataFrame with latitude and longitude values

    run_df = df[df["activity_type__type_key"] == "running"]
    run_df = run_df[['start_latitude', 'start_longitude']]

    ## Create a map with the data    
    run_df.columns = ['latitude', 'longitude']
    ## Create a map with the data
    st.map(run_df)

