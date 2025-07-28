import json

locations_data = []
with open('shopping_malls.json', 'r', encoding='utf-8') as file:
    parsed = json.load(file)

for idx, place_data in enumerate(parsed['places']):
    place_name = place_data['displayName']['text']
    latitude= place_data['location']['latitude']
    longitude = place_data['location']['longitude']
    locations_data.append([idx, place_name, latitude, longitude])


with open('../constants.py', 'a', encoding='utf-8') as f:
    f.write("LOCATIONS = [\n")
    for idx, name, latitude, longitude in locations_data:
        f.write(f"    ( {idx}, '{name}', '{latitude}', '{longitude}'),\n")
    f.write("]\n")




