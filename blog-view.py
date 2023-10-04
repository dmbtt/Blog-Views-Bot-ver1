import requests
import time
import sys
from stem import Signal
from stem.control import Controller

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
}

print("""\033[1m\033[37m
     _____ ___  ____            ____  _              __     ___                     ____        _                                                     
    |  ___/ _ \/ ___|          | __ )| | ___   __ _  \ \   / (_) _____      _____  | __ )  ___ | |_                                                   
    | |_ | | | \___ \   _____  |  _ \| |/ _ \ / _` |  \ \ / /| |/ _ \ \ /\ / / __| |  _ \ / _ \| __|                                                  
    |  _|| |_| |___) | |_____| | |_) | | (_) | (_| |   \ V / | |  __/\ V  V /\__ \ | |_) | (_) | |_                                                   
    |_|   \___/|____/          |____/|_|\___/ \__, |    \_/  |_|\___| \_/\_/ |___/ |____/ \___/ \__|                                                  
                                              |___/                                                                                                  
                                                                     \033[41m FOS- Fools of Security :)
\033[0m
""")

# Default Tor port configuration
proxyPort = 9050
ctrlPort = 9051
site = input("Enter your Blog Address: ")
blog = int(input("Enter The number of Viewers: "))


def run():
    with Controller.from_port(port=ctrlPort) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
    response = requests.get(site, headers=headers, verify=False)
    print("[" + str(i) + "] Blog View Added With IP: " + requests.get('http://ipecho.net/plain').text)


if __name__ == '__main__':
    if len(sys.argv) > 2:
        proxyPort = int(sys.argv[1])
        ctrlPort = int(sys.argv[2])
    for i in range(blog):
        run()
