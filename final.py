import requests

response = requests.get('https://api.tradier.com/v1/markets/history',
    params={'symbol': 'AAPL', 'interval': 'daily', 'start': '2025-07-30', 'end': '2025-07-30', 'session_filter': 'all'},
    headers={'Authorization': 'Bearer SWTHKIdMhs8swYpV42W6qBGay1JR', 'Accept': 'application/json'}
)
json_response = response.json()
print(response.status_code)
print(json_response)


import requests

response = requests.get('https://api.tradier.com/v1/markets/quotes',
    params={'symbols': 'AAPL,VXX190517P00016000', 'greeks': 'false'},
    headers={'Authorization': 'Bearer SWTHKIdMhs8swYpV42W6qBGay1JR', 'Accept': 'application/json'}
)
json_response = response.json()
print(response.status_code)
print(json_response)

import requests

response = requests.get(
    'https://api.tradier.com/v1/markets/timesales',
    params={
        'symbol': 'AAPL',
        'interval': '5min',
        'start': '2025-07-30 09:30',
        'end': '2025-07-30 16:00',
        'session_filter': 'all'
    },
    headers={
        'Authorization': 'Bearer SWTHKIdMhs8swYpV42W6qBGay1JR',
        'Accept': 'application/json'
    }
)
print(response.status_code)
print(response.json())

import requests

url = "https://api.tradier.com/v1/markets/timesales"

params = {
    "symbol": "SPY",
    "interval": "1min",
    "start": "2025-07-29T14:00:00",  # Adjust to recent trading hours
    "end": "2025-07-29T15:00:00",
    "session_filter": "all"
}

headers = {
    "Authorization": "Bearer SWTHKIdMhs8swYpV42W6qBGay1JR",
    "Accept": "application/json"
}

response = requests.get(url, params=params, headers=headers)
print("Status:", response.status_code)
print("Raw response:", response.text)

# Only try to parse JSON if response is successful
if response.status_code == 200:
    data = response.json()
    print("Parsed JSON:", data)
else:
    print("Failed to fetch data from Tradier. Check your token and parameters.")

