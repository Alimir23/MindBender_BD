import requests
from kafka import SimpleProducer, KafkaClient
import json

TOPIC = "covidapi"

url = 'https://api.covidtracking.com/v1/states/current.json'

response = requests.request("GET", url)

text = response.text

kafka = KafkaClient("localhost:9099")

producer = SimpleProducer(kafka)

producer.send_messages(TOPIC, text.encode("UTF-8"))




