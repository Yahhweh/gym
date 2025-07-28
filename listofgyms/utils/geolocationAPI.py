import requests
import json
from decouple import config

def get_shopping_malls(api_key):
    url = "https://places.googleapis.com/v1/places:searchNearby"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.location"
    }

    payload = {
        "includedTypes": ["shopping_mall"],
        "maxResultCount": 40,
        "locationRestriction": {
            "circle": {
                "center": {"latitude": 50.4501, "longitude": 30.5234},
                "radius": 10000.0
            }
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()



api_key = config('API_KEY')
result = get_shopping_malls(api_key)


with open('shopping_malls.json', 'w') as f:
    json.dump(result, f, indent=2)
