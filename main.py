#!/usr/bin/env python
import psutil
import requests
import os.path
import time
import cpuinfo
import uuid
import webbrowser

# gives a single float value
#print(psutil.sensors_battery())

#print(psutil.net_io_counters())

device_uuid = ""
url = "https://2c94-46-253-188-135.eu.ngrok.io"


def is_installed():
    global device_uuid

    if os.path.isfile("setup.ini"):
        f = open("setup.ini", "r")
        temp = f.read()
        if temp != "":
            device_uuid = temp
            f.close()
            return True
        f.close()
    return False


def install():
    global device_uuid
    device_uuid = str(uuid.uuid4())
    f = open("setup.ini", "w")
    f.write(device_uuid)
    f.close()
    webbrowser.open(url+'/login?'+device_uuid)
    return


# main

if not is_installed():
    install()

data = {'uuid': device_uuid}


while 1:
    data["ts"] = time.time()
    data["cpu_name"] = cpuinfo.get_cpu_info()['brand_raw']
    data["cpu_freq"] = psutil.cpu_freq()[0]
    data["cpu_load"] = psutil.cpu_percent(interval=1, percpu=False)
    requests.post(url+"/ingest", json=data)
    time.sleep(10)



#requests.post(url, data={key: value}, json={key: value}, args)

