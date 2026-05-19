

import csv
import os


STOCK_PRICES = {
    "AAPL":  182.50,   
    "TSLA":  248.00,   
    "GOOGL": 175.30,   
    "AMZN":  192.00,   
    "MSFT":  415.00,   
    "INFY":   19.80,   
    "TCS":    65.00,   
}


def show_available_stocks():
    print("\n📈 Available Stocks:")
    print(f"  {'Symbol':<8} {'Company':<12} {'Price (USD)':>12}")
    print("  " + "-" * 34)

    company_names = {
        "AAPL": "Apple", "TSLA": "Tesla", "GOOGL": "Google",
        "AMZN": "Amazon", "MSFT": "Microsoft", "INFY": "Infosys", "TCS": "TCS"
    }

    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<8} {company_names[symbol]:<12} ${price:>10.2f}")


def collect_portfolio():
    
    portfolio = []  
    print("\n💼 Enter your stock holdings.")
    print("   Type 'done' when finished.\n")

    while True:
        symbol = input("   Stock symbol (e.g. AAPL): ").strip().upper()

        if symbol == "DONE":
            if len(portfolio) == 0:
                print("   ⚠  Please add at least one stock first.")
                continue
            break  

        if symbol not in STOCK_PRICES:
            print(f"   ⚠  '{symbol}' not found. Choose from the list above.")
            continue

        try:
            qty = int(input(f"   Quantity of {symbol}: ").strip())
            if qty <= 0:
                print("   ⚠  Quantity must be a positive number.")
                continue
        except ValueError:
            print("   ⚠  Please enter a valid whole number.")
            continue

        portfolio.append((symbol, qty)) 
        print(f"   ✅ Added {qty} share(s) of {symbol}.\n")

    return portfolio


def calculate_and_display(portfolio):
    
    print("\n" + "=" * 50)
    print("        📊 YOUR PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"  {'Stock':<8} {'Qty':>5} {'Price':>10} {'Total Value':>13}")
    print("  " + "-" * 40)

    results = []      
    grand_total = 0.0 

    for symbol, qty in portfolio:
        price = STOCK_PRICES[symbol]        
        total_value = price * qty            
        grand_total += total_value           

        print(f"  {symbol:<8} {qty:>5} ${price:>9.2f} ${total_value:>12.2f}")

        results.append({
            "Stock": symbol,
            "Quantity": qty,
            "Price (USD)": price,
            "Total Value (USD)": round(total_value, 2)
        })

    print("  " + "-" * 40)
    print(f"  {'TOTAL':<25} ${grand_total:>12.2f}")
    print("=" * 50)
    print(f"\n  💰 Total Portfolio Value: ${grand_total:,.2f}")

    return results, grand_total


def save_to_csv(results, grand_total):
    
    filename = "portfolio_summary.csv"

    with open(filename, "w", newline="") as file:
        fieldnames = ["Stock", "Quantity", "Price (USD)", "Total Value (USD)"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()       
        writer.writerows(results)

        
        writer.writerow({
            "Stock": "TOTAL",
            "Quantity": "",
            "Price (USD)": "",
            "Total Value (USD)": round(grand_total, 2)
        })

    print(f"\n  💾 Portfolio saved to '{filename}' successfully!")
    print(f"  📂 Location: {os.path.abspath(filename)}")


def main():
    print("\n" + "=" * 50)
    print("    📈 STOCK PORTFOLIO TRACKER — CodeAlpha")
    print("=" * 50)

    show_available_stocks()       
    portfolio = collect_portfolio()  
    results, grand_total = calculate_and_display(portfolio)  
    save = input("\n  Save results to CSV file? (y/n): ").strip().lower()
    if save == "y":
        save_to_csv(results, grand_total)

    print("\n  Thank you for using Stock Portfolio Tracker! 👋\n")


if __name__ == "__main__":
    main()