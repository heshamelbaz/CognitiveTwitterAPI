#!/usr/bin/python

## THIS FILE IS FOR TESTING PURPOSES ONLY - WILL BE IGNORED LATER ##

import clustering
import requests
import json

payload = {
    'city': 'London',
    'query': 'Arsenal'
}
headers = {
    'Content-Type': 'application/json',
    'Accepts': 'application/json'
}
r = requests.post('http://127.0.0.1:3000/', data=json.dumps(payload), headers=headers)

corpus = [tweet['text'] for tweet in r.json()]
print clustering.cluster_documents(corpus)