import time
import requests
from db_utils import init_db, store_price

PRICE_CHECK_INTERVAL = 180  # seconds

def get_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data['bitcoin']['usd']

def run_bot():
    print("Running bot...")
    price = get_price()
    print(f"Fetched price: ${price}")
    store_price(price)




# main function, to run program every time interval
if __name__ == "__main__":
    init_db()
    while True:
        run_bot()
        time.sleep(PRICE_CHECK_INTERVAL)  # 3 minutes
