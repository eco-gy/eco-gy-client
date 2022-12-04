#!/usr/bin/env python
import psutil
import requests
import os.path
import time
import cpuinfo
import webbrowser
import socket


device_uuid = ""
url = "https://api.eco.gy"
url_login = "https://eco.gy"


def is_installed():
    global device_uuid

    if os.path.isfile("setup.ini"):
        f = open("setup.ini", "r")
        temp = f.read()
        f.close()
        if temp != "":
            respond = requests.post(url+"/checkdevice", json={'device_id': temp})
            if respond.text == "ok":
                device_uuid = temp
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
    browser_url = url_login+'/login?device_uuid='+device_uuid
    print(browser_url)
    webbrowser.open(browser_url)
    return


# main
def main():
    if not is_installed():
        install()

    data = {'uuid': device_uuid}
    hostname = socket.gethostname()

    while 1:
        data["ts"] = time.time()
        try:
            data["cpu_name"] = cpuinfo.get_cpu_info()['brand_raw']
        except:
            pass

        try:
            data["cpu_freq"] = psutil.cpu_freq()[0]
        except:
            pass

        try:
            data["cpu_load"] = psutil.cpu_percent(interval=1, percpu=False)
        except:
            pass

        try:
            data["hostname"] = hostname
        except:
            pass

        requests.post(url+"/ingest", json=data)
        time.sleep(0.1)


main()
