stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 300
}

total_investment = 0

print("Stock Portfolio Tracker")

n = int(input("How many stocks do you want to add? "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        value = stock_prices[stock] * quantity
        total_investment += value
        print(f"{stock} added! Value = {value}")
    else:
        print("Stock not found!")

print("\nTotal Investment Value:", total_investment)