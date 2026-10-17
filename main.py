buyers = [
    {"name": "Jane", "max_price": 10},
    {"name": "John", "max_price": 15},
]

sellers = [
    {"name": "Alice", "min_price": 7},
    {"name": "Bob", "min_price": 12},
]

if buyers[0]["max_price"] >= sellers[0]["min_price"]:
    trade_price = sellers[0]["min_price"]
    print("Jane and Alice can make a trade.")
    print(f"Trade price: {trade_price}")
else:
    print("Jane and Alice cannot make a trade.")