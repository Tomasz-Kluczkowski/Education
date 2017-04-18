import time
from _datetime import datetime as dt
import ctypes
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAmin()
    except:
        return False

if is_admin():

    # hosts_temp = r"hosts"
    # hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    hosts_path = r"hosts"
    redirect_IP = "127.0.0.1"
    websites_to_block = ["www.facebook.com", "facebook.com", "https://outlook.live.com/owa/", "outlook.live.com"]

    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
            print("Working hours...")
            with open(hosts_path, "r+") as file:
                content = file.read()
                for website in websites_to_block:
                    if website in content:
                        pass
                    else:
                        file.write(redirect_IP + " " + website + "\n")
        else:
            with open(hosts_path, "r+") as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in websites_to_block):
                        file.write(line)
                file.truncate()

    time.sleep(5)
else:
    # rerun the program with Admin rights
    ctypes.windll.shell32.ShellExecuteW(None, u"runas", sys.executable, sys.argv[0], None, 1)