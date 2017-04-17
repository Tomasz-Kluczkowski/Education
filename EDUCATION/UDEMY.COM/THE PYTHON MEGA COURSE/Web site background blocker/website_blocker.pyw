import time
from _datetime import datetime as dt

hosts_temp = r"hosts"
# hosts_path = r"C:\Windows\System32\drivers\etc"
redirect_IP = "127.0.0.1"
websites_to_block = ["www.facebook.com", "facebook.com", "https://outlook.live.com/owa/", "outlook.live.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours...")
        with open(hosts_temp, "r+") as file:
            content = file.read()
            for website in websites_to_block:
                if website in content:
                    pass
                else:
                    file.write(redirect_IP + " " + website + "\n")
    else:
        with open(hosts_temp, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_to_block):
                    file.write(line)
            file.truncate()

    time.sleep(5)