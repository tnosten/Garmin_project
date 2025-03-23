# **Garmin Data Engineering Project**

This project extracts, transforms, and visualizes running activity data from the **Garmin API** and stores it in **DuckDB** for analysis. It includes a **Streamlit dashboard** for visualization and **GitHub Actions CI/CD** for automation.

---

## **Project Overview**

### **Features**  
- Extracts activity data using the **Garmin API** (with potential support for **Strava API**)  
- Stores structured data in **DuckDB** for efficient querying  
- Implements **best-effort tracking** (1K, 5K, and 1 Mile times)  
- Provides a **Streamlit dashboard** for interactive data visualization  
- Automates **CI/CD** with **GitHub Actions** for linting, testing, and ingestion  

---

## **Project Structure**

```
Garmin_project-main/
│── .github/workflows/   # CI/CD automation
│── src/
│   ├── ingestion/       # Data extraction scripts
│   ├── analysis/        # Querying and transformations
│   ├── utils/           # Helper functions (if needed)
│── tests/               # Unit & integration tests
│── data/                # Ignored (stores local DB files)
│── app.py               # Streamlit dashboard
│── requirements.txt     # Dependencies
│── README.md            # Documentation
```

---

## **Data Ingestion**

To fetch data from the Garmin API and store it in DuckDB, run:  
```bash
python src/ingestion/garmin_ingest.py
```
This script retrieves the latest **Garmin activities** and updates the local database file.

---

## **Running the Streamlit Dashboard**

To launch the Streamlit app, use:  
```bash
streamlit run app.py
```
This will open an interactive dashboard displaying best-effort running times and a map of running activities.

---

## **CI/CD with GitHub Actions**

This project includes automated workflows:

- **`ci.yml`** – Runs linting and tests  
- **`ingest.yml`** – Fetches data from the Garmin API  

### **Running Tests Locally**
To ensure data integrity and correct API behavior, run:  
```bash
pytest tests/
```

---

## **Installation & Setup**

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/Garmin_project.git
   cd Garmin_project
   ```

2. Set up a virtual environment and install dependencies:  
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # OR
   .venv\Scripts\activate  # Windows

   pip install -r requirements.txt
   ```

3. Configure credentials:  
   - Create a `.env` file with your **Garmin API credentials**

---

## **Future Improvements**
- Add Strava API ingestion  
- Improve best-effort calculations  
- Enhance CI/CD with scheduled ingestion runs  

