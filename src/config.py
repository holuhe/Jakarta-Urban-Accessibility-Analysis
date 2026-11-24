import os
from pathlib import Path
import requests

def find_project_root():
    current = Path.cwd()

    for path in [current, *current.parents]:
        if (path / ".git").exists():
            return path

    raise FileNotFoundError("Project root not found")


PROJECT_ROOT = find_project_root()

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

OUTPUT_DIR = PROJECT_ROOT / "outputs"

API_KEY = os.getenv("GEOAPIFY_API_KEY")

def geocode_address(address):
    if not address:
        return None

    url = "https://api.geoapify.com/v1/geocode/search"

    params = {
    "text": f"{address}, Jakarta, Indonesia",
    "filter": "countrycode:id",
    "format": "json",
    "limit": 1,
    "apiKey": API_KEY
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()

    if not data["results"]:
        return None

    result = data["results"][0]

    coordinates = {
        "latitude": result["lat"],
        "longitude": result["lon"]
    }

    return coordinates

   
