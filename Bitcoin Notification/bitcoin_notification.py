import requests
bitcoin_api_url = 'https://api.coingecko.com/api/v3/coins/bitcoin'
response = requests.get(bitcoin_api_url)
print(response.status_code)

response_json = response.json()

print(response_json)