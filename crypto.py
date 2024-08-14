import websocket
import json

# Define the trading pair you want to track
symbol = "btcusdt"

# Define the WebSocket URL for Binance
url = f"wss://stream.binance.com:9443/ws/{symbol}@trade"

def on_message(ws, message):
    data = json.loads(message)
    price = data["p"]
    print(f"Price: {price}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("Closed")

def on_open(ws):
    print(f"Connected to {symbol} live price feed")

if __name__ == "__main__":
    ws = websocket.WebSocketApp(url, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
