#!/usr/bin/env python
import psutil
import requests
import os.path
import time
# gives a single float value
#print(psutil.sensors_battery())

#print(psutil.net_io_counters())


api_key = 0


def is_installed():
    global api_key
    if os.path.isfile("setup.ini"):
        f = open("setup.ini", "r")
        temp = f.read()
        if temp != "":
            api_key = temp
            f.close()
            return True
        f.close()
    return False


def install():
    return


if not is_installed():
    install()

data = {'uuid': api_key}
url = "https://eco-gy.herokuapp.com/ingest"

while 1:
    data["ts"] = time.time()
    data["cpu_freq"] = psutil.cpu_freq()[0]
    data["cpu_load"] = psutil.cpu_percent(interval=1, percpu=False)
    requests.post(url, json=data)
    time.sleep(10)



#requests.post(url, data={key: value}, json={key: value}, args)

