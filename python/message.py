
import requests
import json
import hashlib
import calendar
import time
import os


def get_au(md5_raw_str):
    md5 = hashlib.md5()
    md5.update(md5_raw_str)
    return md5.hexdigest()


def get_news():
    url = "http://sailor.kfcex.com/api/api/v1/cpbox/cpNews/last"
    current_gmt = time.gmtime()
    time_stamp = calendar.timegm(current_gmt)

    au = get_au(("WePlatformCRh5cf#Dg5Q4qw@Z7FtxwDWH" +
                str(time_stamp)).encode('utf-8'))
    payload = json.dumps({
        "Au": au,
        "Platform": "WePlatform",
        "Timestamp": time_stamp
    })
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    res = json.loads(response.text)
    if res["code"] != 0:
        return []
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
        for element in res['data']["list"]:
            if element["id"] > maxid:
                rstlist.append(element)
                if element["id"] > newmaxid:
                    newmaxid = element["id"]

        ff.close()
    if newmaxid > maxid:
        with open(filename, "w+") as ff:
            ff.write('%d\n' % (newmaxid))
            ff.close()

    return rstlist


if __name__ == '__main__':
    get_news()

# get_news()
