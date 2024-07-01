from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import csv



key = '7b2a49d7-1570-4575-8977-9f920f3b2a69'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'100',
  'convert':'RUB'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': key,
}

session = Session()
session.headers.update(headers)
with open('cmc_top.csv', 'w', newline='', encoding="utf-8") as file:
  count = 0
  writer = csv.writer(file)
  writer.writerow(
    ['Rank', 'Name', 'Price', 'Market Cap', 'Volume (24h)', 'Circulating Supply', 'Change (24h)', 'Change (7d)',
     'Change (1h)'])
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  for i in data['data']:
    count += 1
    quote = i['quote']['RUB']
    writer.writerow([count,i['name'],quote['price'],quote['market_cap'],quote['volume_24h'],i['circulating_supply'],quote['percent_change_24h'],quote['percent_change_7d']])

