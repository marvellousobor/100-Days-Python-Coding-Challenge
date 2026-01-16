import requests
API_KEY = "6e62efc9e6834736a96c2f6fa4909f4a"

def get_crypto_price(symbol):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    headers = {
        "X-CMC_PRO_API_KEY": API_KEY,
        "Accept": "application/json"
    }
    params = {"symbol": symbol}
    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        if response.status_code != 200:
            print(f"Error. Something went wrong {response.status_code}")
            return

        price = data["data"][symbol]["quote"]["USD"]["price"]
        name = data["data"][symbol]["name"]
        print(f"\n{name} ({symbol}) Price: ${price:,.2f}")

    except Exception as e:
        print("An error occurred:", e)

crypto = input("Enter a crypto symbol (BTC, ETH, SOL, BNB, etc.): ").upper()
get_crypto_price(crypto)
