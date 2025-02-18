# Garmin_project
objective: Extract data from garmin device and create dashboard with some analytics

Data sources:
garmin connect (API)
Strava (API)
Stryd (unknown)
garmin lifestyle data?
...

Data ingestion using DLT

Clean data (data quality enforcement)

Load data into duckdb

Model the data and clean using duckdb transformations

Load into Streamlit for dashboard





About the structure of the repo:

- setup.ps1 contains the powershell scripts that are used to set the project up
- requirements.txt contains all the dependencies
- gitignore is to ignore the .venv folder and .env from being commited into github
- .env is to store environment variables (username &password)
- src folder contains the main source code (to be developed further)
- data contains the actual data (should be built out into medalion structure?)
- .venv is the virtual environment to make the dependencies (library ,python version) consistent
