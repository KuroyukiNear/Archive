import json
import requests


def fetch_data(*, update: bool = False, json_cache: str, url: str):
    if update:
        json_data = None

    else:
        try:
            with open(json_cache, "r") as file:
                json_data = json.load(file)
                print("Fetched data from local cache.")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"No local cache found... ({e})")
            json_data = None

    if not json_data:
        print("Fetching new json data... (Creating local cache)")
        json_data = requests.get(url).json()
        with open(json_cache, "w") as file:
            json.dump(json_data, file, indent=2)

    return json_data


if __name__ == "__main__":
    url = "https://kuroyukinear.github.io/JSON_data/discord_id.json"
    json_cache = "cache.json"

    data: dict = fetch_data(update=True, json_cache=json_cache, url=url)
    print(data)
