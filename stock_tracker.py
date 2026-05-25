# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330,
    "AMZN": 145
}

total_investment = 0

print(" Stock Portfolio Tracker")

# Number of stocks user wants to enter
n = int(input("Enter number of stocks: "))

# Store portfolio details
portfolio = []

for i in range(n):

    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        stock_value = stock_prices[stock_name] * quantity

        total_investment += stock_value

        portfolio.append(
            f"{stock_name} - Quantity: {quantity} - Value: ${stock_value}"
        )

    else:
        print(" Stock not available!")

# Display Result
print("\n Portfolio Summary")

for item in portfolio:
    print(item)

print(f"\n Total Investment Value: ${total_investment}")

# Save to text file
with open("portfolio.txt", "w") as file:

    file.write("Stock Portfolio Summary\n\n")

    for item in portfolio:
        file.write(item + "\n")

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\nPortfolio saved to portfolio.txt")
