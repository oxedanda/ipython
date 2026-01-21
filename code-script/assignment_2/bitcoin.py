import sys
import requests


def main():
    # Check if the user provided a command-line argument
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        # Convert the argument to float
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Your API key here
    api_key = "S0e96e6f850fc22400db9ebbd5529d4f9a579e086615d1d7b43cd930155febd02"

    # CoinCap v3 API URL
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Network error")

    # Parse JSON and get the price
    data = response.json()
    price = float(data["data"]["priceUsd"])

    # Calculate total
    total = bitcoins * price

    # Print formatted result
    print(f"${total:,.4f}")


main()