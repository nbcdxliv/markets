buyers = [
    {"name": "Jane", "max_price": 10},
    {"name": "John", "max_price": 15},
]

sellers = [
    {"name": "Alice", "min_price": 7},
    {"name": "Bob", "min_price": 12},
]

for buyer in buyers:
    for seller in sellers:
        if buyer["max_price"] >= seller["min_price"]:
            trade_price = seller["min_price"]
            print(
                f'{buyer["name"]} and {seller["name"]} can trade '
                f'at {trade_price}.'
            )
        else:
            print(f'{buyer["name"]} and {seller["name"]} cannot trade.')