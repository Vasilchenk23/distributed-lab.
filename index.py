def calculate_capital(N, C, gains, prices):
    profit_per_laptop = [(gains[i] - prices[i]) for i in range(len(gains))]
    sorted_laptops = sorted(range(len(gains)), key=lambda i: profit_per_laptop[i], reverse=True)
    
    total_capital = C
    bought_laptops = 0
    
    for i in sorted_laptops:
        if bought_laptops < N and total_capital >= prices[i]:
            total_capital += profit_per_laptop[i]
            bought_laptops += 1
    
    return total_capital

def main():
    N = int(input("Enter the maximum number of laptops to buy (N): "))
    C = float(input("Enter the initial capital (C): "))
    
    gains = []
    prices = []
    for i in range(N):
        print(f"Information about laptop {i+1}:")
        gain = float(input("Enter the gain: "))
        price = float(input("Enter the price: "))
        gains.append(gain)
        prices.append(price)
    
    capital = calculate_capital(N, C, gains, prices)
    print(f"Capital at the end of the summer: {capital}")

if __name__ == "__main__":
    main()
