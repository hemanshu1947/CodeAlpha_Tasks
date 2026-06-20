# Simple Stock Tracker

# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

total_investment = 0
portfolio = {}

# Taking user input
n = int(input("Enter number of stocks you want to add: "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    # Check if stock exists
    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        portfolio[stock_name] = {
            "quantity": quantity,
            "investment": investment
        }
    else:
        print("Stock not found in price list!")

# Display portfolio details
print("\n----- Portfolio Summary -----")

for stock, details in portfolio.items():
    print(f"{stock} -> Quantity: {details['quantity']}, "
          f"Investment: ${details['investment']}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional file saving
choice = input("\nDo you want to save the report? (yes/no): ").lower()

if choice == "yes":
    file_type = input("Save as txt or csv? ").lower()

    if file_type == "txt":
        with open("portfolio_report.txt", "w") as file:
            file.write("Portfolio Summary\n")
            file.write("-------------------\n")

            for stock, details in portfolio.items():
                file.write(
                    f"{stock} -> Quantity: {details['quantity']}, "
                    f"Investment: ${details['investment']}\n"
                )

            file.write(f"\nTotal Investment Value: ${total_investment}")

        print("Report saved as portfolio_report.txt")

    elif file_type == "csv":
        with open("portfolio_report.csv", "w") as file:
            file.write("Stock,Quantity,Investment\n")

            for stock, details in portfolio.items():
                file.write(
                    f"{stock},{details['quantity']},"
                    f"{details['investment']}\n"
                )

            file.write(f"\nTotal Investment,,{total_investment}")

        print("Report saved as portfolio_report.csv")

    else:
        print("Invalid file type selected.")