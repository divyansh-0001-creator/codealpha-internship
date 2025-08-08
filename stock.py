# Hardcoded stock prices



stock_prices = {"AAPL" : 180, "TSLA" : 250 , "GOOGL" : 130 , "AMZN" : 140 , "MSFT" : 320 , "FLKRT" : 110 , "JIO" : 220 , "ADANI" : 190 , "ICICI" : 150 , "ZOMATO" : 175 ,}

# Dictionary to store user input

portfolio = {}
total_investment = 0

# Input loop

while True:
    stock = input("Enter stock symbol (or type 'done' to finish):\n ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment

print("\n--- Investment Summary ---")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\nTotal Investment: ${total_investment}")

# Optionally save to file

save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter filename (with .txt or .csv extension): ")
    with open(filename, "w") as file:
        file.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock},{qty},{price},{value}\n")
        file.write(f"\nTotal Investment,,,{total_investment}\n")
    print(f"Investment summary saved to '{filename}'.")

          
          
          
          
          
        
                       
        

    
