import time
from datetime import datetime as dt

# C:\Windows\System32\drivers\etc
host_temp = "hosts"
host_path = r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"
# Change those to your selected websites
website_list = ["www.facebook.com", "facebook.com", "fb.com",
                "www.google.com", "google.com", "www.youtube.com", "youtube.com"]

# Change those to your selected hour
start_hour = 8
end_hour = 16

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, start_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_hour):
        print("Working hours...")
        with open(host_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" " + website + "\n")
    else:
        with open(host_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
            print("Not in the Working hours...")
    time.sleep(5)
