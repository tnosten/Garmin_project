
from garminconnect import Garmin
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

load_dotenv()

# # Update with your own credentials


username = os.getenv("GARMIN_USERNAME")
password = os.getenv("GARMIN_PASSWORD")


# print(username, password)  # Check if it works



# Connect to the API
try:
    api = Garmin(username, password)
    login_status = api.login()  # This should return True or False
    if not login_status:
        raise Exception("Login failed. Please check your credentials.")
except Exception as e:
    print(f"An error occurred while initializing the API: {e}")
    exit(1)  # Exit if login fails

# Set the start and end date
activity_start_date = datetime.date(2023, 1, 1)
activity_end_date = datetime.date(2025, 9, 30)

# Call the API and create a list of activities from that timeframe
try:
    activities = api.get_activities_by_date(
                    activity_start_date.isoformat(),
                    activity_end_date.isoformat()
    )
except Exception as e:
    print(f"An error occurred while fetching activities: {e}")
    activities = None

# # Check if activities were fetched successfully
# if activities:
#     print(f"Retrieved {len(activities)} activities.")
# else:
#     print("No activities found.")



## store the activities into df
if activities:
    # Convert activities to a DataFrame (example, adjust based on your activity data structure)
    df = pd.DataFrame(activities)
    print(df.head())  # Show the first few rows




if activities:
    # Example: Visualize total distance vs. date
    df['date'] = pd.to_datetime(df['startTimeLocal'])  # Assuming 'startTimeLocal' is available
    df['distance'] = df['distance']  # Assuming 'distance' is in meters

    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['distance'])
    plt.title('Total Distance per Activity')
    plt.xlabel('Date')
    plt.ylabel('Distance (meters)')
    plt.xticks(rotation=45)
    plt.show()



    # # Optionally, save the activities to a CSV
    # df.to_csv('activities.csv', index=False)