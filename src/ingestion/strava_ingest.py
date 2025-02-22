import dlt
import requests
from typing import Any, Optional
from dlt.sources.rest_api import (
    RESTAPIConfig,
    check_connection,
    rest_api_resources,
    rest_api_source,
)

STRAVA_API_URL = "https://www.strava.com/api/v3"

dlt.secrets._secrets_storage = None  # This resets the in-memory cache


@dlt.source(name="strava")
def strava_source(
    access_token: Optional[str] = dlt.secrets["access_token"], 
    refresh_token: Optional[str] = dlt.secrets["refresh_token"], 
    client_id: Optional[str] = dlt.secrets["customer_id"], 
    client_secret: Optional[str] = dlt.secrets["customer_secret"]
) -> Any:
    # Refresh the access token if needed
    if not access_token or is_token_expired():
        access_token = refresh_access_token(refresh_token, client_id, client_secret)
    
    config: RESTAPIConfig = {
        "client": {
            "base_url": STRAVA_API_URL,
            "auth": {
                "type": "bearer",
                "token": access_token,
            },
        },
        "resource_defaults": {
            "primary_key": "id",
            "write_disposition": "merge",
            "endpoint": {
                "params": {
                    "per_page": 100,
                },
            },
        },
        "resources": [
            {
                "name": "activities",
                "endpoint": {
                    "path": "athlete/activities",
                    "params": {
                        "after": {
                            "type": "incremental",
                            "cursor_path": "start_date",
                            "initial_value": "2024-01-01T00:00:00Z",
                        },
                    },
                },
            },
        ],
    }

    yield from rest_api_resources(config)


def is_token_expired() -> bool:
    """Check if the Strava token is expired (you might need to track expiration)."""
    return False  # Placeholder: track expiration time properly


def refresh_access_token(refresh_token: str, client_id: str, client_secret: str) -> str:
    """Refresh the Strava access token."""
    response = requests.post(
        "https://www.strava.com/oauth/token",
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
        },
    )
    response.raise_for_status()
    new_tokens = response.json()
    
    # Update stored secrets in secrets.toml (not needed, but possible)
    dlt.secrets.update({
        "access_token": new_tokens["access_token"],
        "refresh_token": new_tokens["refresh_token"],
    })
    
    return new_tokens["access_token"]


def load_strava() -> None:
    pipeline = dlt.pipeline(
        pipeline_name="strava_pipeline",
        destination=dlt.destinations.duckdb("./data/strava_pipeline.duckdb"),
        dataset_name="strava_data",
    )

    load_info = pipeline.run(strava_source())
    print(load_info)


if __name__ == "__main__":
    load_strava()







############################

print("Loaded access token:", dlt.secrets.get("access_token"))


import requests


response = requests.get(
    "https://www.strava.com/api/v3/athlete",
    headers={"Authorization": f"Bearer {access_token}"}
)

print(response.json())  # Check if access is limited



import dlt


# Print the token that Python is using
access_token = dlt.secrets.value["strava"]["access_token"]
print(f"Python is using this token: {access_token}")






import dlt

# Force reload secrets
dlt.secrets.reload()

# Print the token dlt is using
print(f"dlt.secrets.value token: {dlt.secrets.value.get('strava', {}).get('access_token')}")
