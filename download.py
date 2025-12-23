import os
import json
import urllib.request

url = "https://textures.neocities.org/manifest.json"

with urllib.request.urlopen(url) as response:
    data = json.load(response)

base_url = data["info"]["base_url"]
texture_path = data["info"]["textures_folder"]

os.makedirs("textures", exist_ok=True)

for catalogue in data["catalogue"]:
    os.makedirs(f"textures/{catalogue['name']}", exist_ok=True)

    for file in catalogue["files"]:
        print(f"- downloading {catalogue['name']}/{file}")
        urllib.request.urlretrieve(f"{base_url}/{texture_path}/{catalogue['name']}/{file}", f"textures/{catalogue['name']}/{file}")

with open("version.txt", "w", encoding="utf-8") as f:
    f.write(str(data["info"]["version"]))
