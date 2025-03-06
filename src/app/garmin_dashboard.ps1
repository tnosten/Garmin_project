

# change to appropriate directory
cd src/ingestion

# run the pipeline
dlt pipeline garmin_pipeline show


# deploy streamlit app
##close ptyhon file first
streamlit run src/analysis/query_duckdb_garmin.py