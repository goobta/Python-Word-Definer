import requests
import time
import json


input_file = "words.txt"
output_file = "wordsAndDefs.txt"

base_api_url = "https://od-api.oxforddictionaries.com/api/v1/entries/"

language = 'en'

app_id = "<your_app_id>"
app_secret = "<your_secret_key>"

cards_delim = "~*~"
terms_delim = "+++"

headers = { "app_id": app_id, "app_secret": app_secret }

with open(input_file, "r") as fh, open(output_file, "w") as out:
    for line in fh:
        word = line.strip().lower()

        url = base_api_url + language + "/" + word
        r = requests.get(url, headers={ "app_id": app_id, "app_key": app_secret })

        res = r.json()

        try:
            out.write(word + terms_delim)

            for entry in res['results']:
                for l in entry['lexicalEntries']:
                    out.write(l['lexicalCategory'] + "\n")
                    for e in l['entries']:
                        for sense in e['senses']:
                            for d in sense['definitions']:
                                out.write(d + "\n")

            out.write(cards_delim)
        except: 
            print("Issue with word: {}".format(word))

        time.sleep(1)
