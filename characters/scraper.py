import requests
from .models import Character

API_URL = "https://rickandmortyapi.com/api/character" # Rick and Morty official API


def scrape_characters():
    url_to_scrape = API_URL

    characters = []

    while url_to_scrape is not None:
        characters_response = requests.get(url_to_scrape).json()

        for character in characters_response["results"]:
            characters.append(
                Character(
                    api_id=character["id"],
                    name=character["name"],
                    species=character["species"],
                    gender=character["gender"],
                    image=character["image"],
                ))

        url_to_scrape = characters_response["info"]["next"]

    return characters


def save_characters(characters):
    for character in characters:
        try:
            character.save()
        except:
            print("Such character already exists")


def sync_characters_with_api():
    characters = scrape_characters()
    save_characters(characters)
