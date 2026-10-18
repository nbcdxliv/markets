buyers = [
    {"name": "Jane", "max_price": 10},
    {"name": "John", "max_price": 15},
]

sellers = [
    {"name": "Alice", "min_price": 9},
    {"name": "Bob", "min_price": 11},
]

remaining_sellers = sellers.copy()
trades = []
total_surplus = 0

for buyer in buyers:
    trade_found = False

    for seller in remaining_sellers:
        if buyer["max_price"] >= seller["min_price"]:
            trade_price = seller["min_price"]
            print(
                f'{buyer["name"]} buys from {seller["name"]} '
                f'at {trade_price}.'
            )
            buyer_surplus = buyer["max_price"] - trade_price
            seller_surplus = trade_price - seller["min_price"]
            total_surplus += buyer_surplus + seller_surplus
            print(f' Buyer surplus: {buyer_surplus}, Seller surplus: {seller_surplus}')
            trades.append((buyer["name"], seller["name"], trade_price)) 
            remaining_sellers.remove(seller)
            trade_found = True
            break

    if not trade_found:
        print(f'{buyer["name"]} could not find a seller.')

print("\nTrade summary:")
for buyer_name, seller_name, price in trades:
    print(f"{buyer_name} bought from {seller_name} for {price}.")

print(f"Total trades: {len(trades)}")
print(f"Total surplus: {total_surplus}")