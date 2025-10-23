import sys #for reading command-line arguments and exiting the program
import requests #for making HTTP requests to the CoinCap API

#your personal CoinCap API key
API_KEY = "a9701372934f03b7bdd9d191ec68344dd0b21e4907c9f08e085ca38f6372a91b"
#base URL for the CoinCap Bitcoin price endpoint
URL = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"


def main():
    #get the number of bitcoins from the command-line
    amount = get_amount()
    #get the current bitcoin price in USD from the CoinCap API
    price = get_bitcoin_price()
    #calculate the total cost in USD
    total = amount * price
    #print the result formatted with commas and 4 decimal places
    print(f"${total:,.4f}")


def get_amount():
    #check if exactly one command-line argument was provided
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        value = float(sys.argv[1])
        return value
    except ValueError:
        #if it fails (if the argument isn't a number), exit with an error message
        sys.exit("Command-line argument is not a number")


def get_bitcoin_price():
    try:
        #send a get request to CoinCap bitcoin endpoint
        response = requests.get(URL)
        response.raise_for_status() #raise an error if the HTTP response is not 200 OK
        #parse the response as JSON (convert from text to a python dict)
        data = response.json()
        #extract the bitcoin price from the JSON response
        #the structure of the JSON is: { "data": { "priceUsd": "XXXXX" }, ... }
        price = float(data["data"]["priceUsd"])
        return price
    except requests.RequestException:
        #handle connection errors, timeouts, or invalid responses
        sys.exit("Error fetching data from CoinCap API")
    except KeyError:
        #handle unexpected response format or missing data
        sys.exit("Unexpected response format from API")


#run the program
if __name__ == "__main__":
    main()
