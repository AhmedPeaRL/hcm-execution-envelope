import os
import time
import requests

# --- Stateless Arbitrage Executor ---
# This execution:
# - reads prices
# - compares asymmetry
# - executes once if condition allows
# - exits silently

EXCHANGE_A_URL = os.getenv("EXCHANGE_A_URL")
EXCHANGE_B_URL = os.getenv("EXCHANGE_B_URL")

API_KEY_A = os.getenv("API_KEY_A")
API_KEY_B = os.getenv("API_KEY_B")

THRESHOLD = float(os.getenv("ARBITRAGE_THRESHOLD", "0.5"))  # percentage

def get_price(url):
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return float(response.json()["price"])

def execute_trade(direction):
    # Placeholder: execution allowed, not optimized
    # No retries, no confirmation loops
    print(f"Execution allowed: {direction}")

def main():
    try:
        price_a = get_price(EXCHANGE_A_URL)
        price_b = get_price(EXCHANGE_B_URL)

        diff = ((price_b - price_a) / price_a) * 100

        if abs(diff) >= THRESHOLD:
            if diff > 0:
                execute_trade("BUY_A_SELL_B")
            else:
                execute_trade("BUY_B_SELL_A")

    except Exception:
        # Silent failure by design
        pass

if __name__ == "__main__":
    main()
