import sys
import requests

# Check if the user provided a command-line argument
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# Convert the argument to float
try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# Make a request to the CoinCap API
try:
    r = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=0e96e6f850fc22400db9ebbd5529d4f9a579e086615d1d7b43cd930155febd02"
    )
except requests.RequestException:
    sys.exit("Network error")

# Extract the price from the JSON response
try:
    data = r.json()
    price = float(data["data"]["priceUsd"])
except (KeyError, TypeError, ValueError):
    sys.exit("Unexpected response")

# Calculate and print the USD value with 4 decimal places and thousand separators
amount = bitcoins * price
print(f"${amount:,.4f}")

