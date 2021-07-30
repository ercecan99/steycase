import websocket, json


def main():
    try:

        levels = '20'
        symbol = 'btcusdt'
        endpoint = f'wss://stream.binance.com:9443/ws/{symbol}@depth{levels}'

        ws = websocket.WebSocketApp(endpoint,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)
        ws.run_forever()
    except Exception as e:
        print(f'An error occurred in main function: {e}')


def on_message(ws, message):
    print(message)
    print("\n"*3)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


if __name__ == '__main__':
    main()