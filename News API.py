import requests
import json

query = input("enter your query: ")
url = f'https://newsapi.org/v2/everything?q={query}&from=&sortBy=publishedAt&language=en&language=hi&apiKey=25ef4ffc7ec3493d892dc4e1ebe9639e'
r = requests.get(url)

news =  json.loads(r.text)
for article in news['articles']:
       print(f"Headline: {article['title']}")
       print(f"Article: {article['description']}")
       print(f"Time at which news is published: {article['publishedAt']}")
       print('--------------------------------------------------------')

