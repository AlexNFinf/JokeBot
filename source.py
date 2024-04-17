#Joke Bot
import requests

with requests.get("https://v2.jokeapi.dev/joke/Any") as joke_response:
  joke_data = joke_response.json()
  if joke_data["type"] == "single":
    print(joke_response.json()['joke'])
  else:
    print(joke_response.json()['setup'])
    print(joke_response.json()['delivery'])
