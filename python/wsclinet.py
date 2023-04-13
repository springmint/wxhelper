import websocket

wsurl = "ws://localhost:8808/ws"


def send_message(txt):
    ws.send(txt)


def on_message(wsapp, message):
    print(wsapp, message)


def on_close(wsapp, cstatus, cmessage):
    print(wsapp, cstatus, cmessage)


def on_error(wsapp, e):
    print(wsapp, e)


def on_open(wsapp):
    wsapp.send("reg")
# def in


def on_ping(wsapp):
    wsapp.send("pong")


def start_websocket_client():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        wsurl, on_message=on_message, on_close=on_close, on_error=on_error, on_open=on_open, on_ping=on_ping)

    ws.run_forever(ping_interval=30)
    # ws.send("reg")


if __name__ == '__main__':
    start_websocket_client()
