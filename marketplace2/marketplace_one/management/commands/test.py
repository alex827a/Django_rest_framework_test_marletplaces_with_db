import requests

# Test authefication with token
token = 'd8b9d3ef06bd1d3f19c8bb1bf34b11a13c759e19'
headers = {'Authorization': f'Token {token}'}

# URL endpoint API
url = 'http://127.0.0.1:8000/api/products/'


response = requests.get(url, headers=headers)

print(response.json())
