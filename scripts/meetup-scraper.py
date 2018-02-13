import requests
import io
from bs4 import BeautifulSoup


# Hardcoded ZIP codes known for their respective categories
categories = {
                'beach':[33109, 32407, 29572, 90266],
                'nightlife':[70130, int('02108'), 10017, 60642],
                'hiking':[98101, 37202, 80303, 84104],
                'architecture':[70130, int('02108'), 98101, 37202]
             }

#TODO see about the jq stuff implemented in the cloud functions
with open('secrets', 'r') as s:
    key = s.readlines()
    key = key[0].strip('\n')

with io.open('meetup_bio_data', 'w', encoding='utf8') as f:
    for topic, locations in categories.items():
        for location in locations:
            endpoint = 'https://api.meetup.com/find/groups?key={}&zip={}&text={}'.format(key, location, topic)
            r = requests.get(endpoint)
            r = r.json() 
            # Group level description
            for group in r:
                description = BeautifulSoup(group['description'], "lxml").text
                description = description.translate({ord(c):None for c in '\r\n\"\''})
                if len(description) > 0:
                    f.write("\"" + description[:1000] + "\""  + "," + topic + '\n')
