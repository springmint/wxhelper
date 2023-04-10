
import requests
import json
import os


def get_news():
    url = "http://sailor.kfcex.com/api/api/v1/cpbox/cpNews/last"
    payload = json.dumps({
        "Au": "dc98570879290a71d975b0d4baf75a03",
        "Platform": "WePlatform",
        "Timestamp": 0
    })
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)
    res = json.loads(response.text)
    filename = "maxid.data"
    maxid = 0
    rstlist = []
    with open(filename, "w+") as ff:
        s = ff.readline()
        if str.strip(s) != "":
            maxid = int(s)
        newmaxid = maxid
        for element in res['data']["list"]:
            if element["id"] > maxid:
                rstlist.append(element)
                if element["id"] > newmaxid:
                    newmaxid = element["id"]

            # print(res['data']["list"].items())
            # if res['code'] == 0:
            # return res['data']["list"].items()
            # return res['code']
        if newmaxid > maxid:
            ff.write('%d\n' % (newmaxid))
        ff.close()
    return rstlist


if __name__ == '__main__':
    get_news()
