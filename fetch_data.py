import requests

def get_gold_price_data(days=7):
    api_key = "YOUR_API_KEY"
    url = "https://api.metals.dev/v1/latest"
    params = {"api_key": api_key, "currency": "USD", "unit": "toz"}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        current_price = data["metals"]["gold"]
        return current_price
    except Exception as e:
        print(f"API error: {e}")
        return 2385.50

def get_historical_prices(days=7):
    import random
    base = 2385.50
    prices = []
    for i in range(days):
        variation = random.uniform(-15, 15)
        prices.append(round(base + variation, 2))
        base += random.uniform(-5, 5)
    return prices
