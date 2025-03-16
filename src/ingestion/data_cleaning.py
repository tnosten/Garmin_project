import pandas as pd
import pandera as pa
from pandera import Column, DataFrameSchema

def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows based on activity ID."""
    return df.drop_duplicates(subset=['activityId'], keep='first')

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Fill or drop missing values in key columns."""
    df = df.dropna(subset=['startTimeLocal', 'distance'])  # Ensure these are always present
    df['calories'].fillna(0, inplace=True)  # Default missing calories to 0
    return df

def normalize_distance(df: pd.DataFrame) -> pd.DataFrame:
    """Convert all distances to kilometers (Garmin uses meters)."""
    df['distance_km'] = df['distance'] / 1000  # Convert meters to km
    return df

def fix_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """Ensure proper data types for key fields."""
    df['startTimeLocal'] = pd.to_datetime(df['startTimeLocal'])  # Convert to datetime
    df['distance_km'] = df['distance_km'].astype(float)  # Ensure distance is float
    return df

def remove_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """Filter out activities with unrealistic values."""
    df = df[df['distance_km'] > 0]  # Remove negative or zero distances
    df = df[df['distance_km'] < 100]  # Assume max 100 km per activity
    return df

def validate_schema(df: pd.DataFrame) -> pd.DataFrame:
    """Validate dataframe schema using Pandera."""
    schema = DataFrameSchema({
        "activityId": Column(int, unique=True),
        "startTimeLocal": Column(pa.DateTime),
        "distance_km": Column(float, checks=pa.Check(lambda x: x > 0)),
        "calories": Column(float, nullable=True)
    })
    return schema.validate(df)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Run all cleaning steps in order."""
    df = drop_duplicates(df)
    df = handle_missing_values(df)
    df = normalize_distance(df)
    df = fix_data_types(df)
    df = remove_outliers(df)
    df = validate_schema(df)
    return df
