import requests

class Portfolio:
    def __init__(self):
        # Initialize the portfolio as an empty dictionary
        self.holdings = {}

    def add_crypto(self, symbol, amount):
        """
        Add a cryptocurrency to the portfolio.
        :param symbol: The symbol of the cryptocurrency (e.g., 'bitcoin')
        :param amount: The amount of the cryptocurrency in the portfolio
        """
        if symbol in self.holdings:
            self.holdings[symbol] += amount  # Add to existing holdings
        else:
            self.holdings[symbol] = amount  # Add new cryptocurrency

    def remove_crypto(self, symbol, amount):
        """
        Remove a cryptocurrency from the portfolio.
        :param symbol: The symbol of the cryptocurrency (e.g., 'bitcoin')
        :param amount: The amount of the cryptocurrency to remove
        """
        if symbol in self.holdings:
            if self.holdings[symbol] >= amount:
                self.holdings[symbol] -= amount
            else:
                print(f"Not enough {symbol} in portfolio.")
        else:
            print(f"{symbol} not found in portfolio.")

    def get_holdings(self):
        """
        Return the current holdings in the portfolio.
        :return: A dictionary with cryptocurrency symbols and amounts
        """
        return self.holdings
