import requests
import time

def get_crypto_price(coin_id="bitcoin"):
    """Fetches the current price of a cryptocurrency in USD."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    
    try:
        response = requests.get(url)
        data = response.json()
        return data[coin_id]['usd']
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def monitor_price(threshold):
    """Monitors the price and prints an alert if it drops below the threshold."""
    print(f"--- Monitoring started. Target: ${threshold} ---")
    
    while True:
        current_price = get_crypto_price()
        
        if current_price:
            print(f"Current Bitcoin Price: ${current_price}")
            
            if current_price <= threshold:
                print("🚨 ALERT: Price is below your target! Time to buy?")
                # In a full project, you'd trigger an email or SMS here.
                break 
        
        # Wait 30 seconds before checking again to avoid rate limiting
        time.sleep(30)

if __name__ == "__main__":
    # Set your 'Buy' alert price here
    my_target = 45000 
    monitor_price(my_target)
