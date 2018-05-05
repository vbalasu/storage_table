import requests, json
import storage_table   #Local storage_table.py
response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,ETH,BTC,INR')
obj = json.loads(response.text)
storage_table.put_object(obj, table_name='ethPrice')
print(obj)
