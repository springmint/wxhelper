import websocket
import json
import os
import time
import threading
from client import send_cpbox_news
wsurl = "ws://sailor.kfcex.com/ws"


def send_message(txt):
    ws.send(txt)


def on_message(wsapp, message):
    print(wsapp, message)
    res = json.loads(message)
    if res["code"] == 1001:
        filename = "maxid.data"
        maxid = 0
        rstlist = []
        if os.path.isfile(filename) == False:
            with open(filename, "w") as fff:
                fff.write("\n")
                fff.close()
        with open(filename, "r+") as ff:
            s = ff.readline()
            if str.strip(s) != "":
                maxid = int(s)
            print('maxID%d' % maxid)
            newmaxid = maxid
            for element in res['data']:
                if element["id"] > maxid:
                    rstlist.append(element)
                    if element["id"] > newmaxid:
                        newmaxid = element["id"]

            ff.close()
        if newmaxid > maxid:
            with open(filename, "w+") as ff:
                ff.write('%d\n' % (newmaxid))
                ff.close()
        send_cpbox_news(rstlist)


def action():
    print("断线重连")
    time.sleep(5)
    ws = websocket.WebSocketApp(
        wsurl, on_message=on_message, on_close=on_close, on_error=on_error, on_open=on_open, on_ping=on_ping)
    ws.run_forever(ping_interval=30)


def on_close(wsapp, cstatus, cmessage):
    # thread = threading.Thread(action)
    # thread.start()
    # print(wsapp, cstatus, cmessage)
    print("断线重连")
    time.sleep(5)
    ws = websocket.WebSocketApp(
        wsurl, on_message=on_message, on_close=on_close, on_error=on_error, on_open=on_open, on_ping=on_ping)
    ws.run_forever(ping_interval=30)


def on_error(wsapp, e):
    print(wsapp, e)


def on_open(wsapp):
    filename = "maxid.data"
    maxid = 0
    with open(filename, "r+") as ff:
        s = ff.readline()
        if str.strip(s) != "":
            maxid = int(s)
    print("reg,%d" % maxid)
    wsapp.send("reg,%d" % maxid)
# def in


def on_ping(wsapp):
    wsapp.send("pong")


def start_websocket_client():
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        wsurl, on_message=on_message, on_close=on_close, on_error=on_error, on_open=on_open, on_ping=on_ping)

    ws.run_forever(ping_interval=30)
    # ws.send("reg")


if __name__ == '__main__':
    start_websocket_client()
    # while (True):
    #     time.sleep(1000)
