prices_input = input("Enter prices separated by space: ")
prices = tuple(map(int, prices_input.split()))

print("Total items sold:", len(prices))
print("Cheapest price:", min(prices))
print("Costliest price:", max(prices))
print("Prices in ascending order:", tuple(sorted(prices)))

costliest = max(prices)
count_costliest = prices.count(costliest)
print("Number of costliest items sold:", count_costliest)