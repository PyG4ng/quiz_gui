import requests

parameters = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}

# General Knowledge, category 9
# Anime and Manga, category 31


response = requests.get("https://opentdb.com/api.php", params=parameters)
question_data = response.json().get("results")
