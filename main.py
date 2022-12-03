#!/usr/bin/env python
import psutil
import requests
import os.path
import time
import cpuinfo
import webbrowser

# gives a single float value
#print(psutil.sensors_battery())

#print(psutil.net_io_counters())

device_uuid = ""
url = "https://api.eco.gy"


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
    # Config
    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZpbmd0cGRtcHNnc3R1emR6eW53Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzAwODQ2MTQsImV4cCI6MTk4NTY2MDYxNH0.JzUxXmGHCjONBbFHN-GIi6kt5oxkBzp0OcxTcOwcmsg',
        'Prefer': 'return=representation'}
    data = {'user_id': 'NULL'}
    supabase_url = 'https://vingtpdmpsgstuzdzynw.supabase.co/rest/v1/device_id'

    # Create new device_id
    resp = requests.post(supabase_url, json=data, headers=headers)

    # Get device_id
    device_uuid = resp.json()[0]['device_id']

    f = open("setup.ini", "w")
    f.write(device_uuid)
    f.close()
    webbrowser.open(url+'/login?device_uuid='+device_uuid)
    return


# main
def main():
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


main()
