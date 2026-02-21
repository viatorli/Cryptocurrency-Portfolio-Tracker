import requests
from portfolio import Portfolio

def get_crypto_price(symbol):
    """
    Fetch the current price of the cryptocurrency from the CoinGecko API.
    :param symbol: The symbol of the cryptocurrency (e.g., 'bitcoin')
    :return: Current price in USD
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    if symbol in data:
        return data[symbol]['usd']
    else:
        print(f"Error: {symbol} not found on CoinGecko.")
        return None

def display_portfolio_value(portfolio):
    """
    Display the total value of the portfolio in USD.
    :param portfolio: The portfolio object that holds cryptocurrency data
    """
    total_value = 0
    holdings = portfolio.get_holdings()
    print("Portfolio Holdings:")
    for symbol, amount in holdings.items():
        price = get_crypto_price(symbol)
        if price is not None:
            value = price * amount
            total_value += value
            print(f"{symbol}: {amount} units, {price} USD each, Value: {value:.2f} USD")
    
    print(f"Total Portfolio Value: {total_value:.2f} USD")

def main():
    """
    Main function to interact with the user and manage the portfolio.
    """
    # Create a portfolio object
    portfolio = Portfolio()

    while True:
        print("\n1. Add Cryptocurrency")
        print("2. Remove Cryptocurrency")
        print("3. View Portfolio Value")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            symbol = input("Enter the cryptocurrency symbol (e.g., bitcoin): ").lower()
            amount = float(input(f"Enter the amount of {symbol} to add: "))
            portfolio.add_crypto(symbol, amount)
        elif choice == "2":
            symbol = input("Enter the cryptocurrency symbol (e.g., bitcoin): ").lower()
            amount = float(input(f"Enter the amount of {symbol} to remove: "))
            portfolio.remove_crypto(symbol, amount)
        elif choice == "3":
            display_portfolio_value(portfolio)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
