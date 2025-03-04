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
df.info()

df.to_csv("output.csv", index=False)  # Save without index

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

