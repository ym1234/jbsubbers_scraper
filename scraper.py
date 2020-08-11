import requests
from time import sleep
import os
from bs4 import BeautifulSoup

base = 'http://jpsubbers.xyz/Japanese-Subtitles/'
log = open('log', 'w', buffering=1)

def mylog(string):
    print(string)
    log.write(string + "\n")

def scrape(URL, prev):
    results = BeautifulSoup(requests.get(URL, allow_redirects=True).content, 'html.parser').find_all('a', href=True)
    for x in results:
        if (base + x['href']) == 'http://jpsubbers.xyz/Japanese-Subtitles/index.php?p=' or (base + x['href']) == prev:
            continue
        mylog("Got url: " + x['href'])
        if 'srt' in x['href'] or 'zip' in x['href']:
            mylog('Downloading: ' + 'http://jpsubbers.xyz/' + x['href'])
            obj = requests.get('http://jpsubbers.xyz/' + x['href'], allow_redirects=True)
            os.makedirs('/'.join(("out" + x['href']).split("/")[0:-1]), exist_ok=True)
            with open("out" + x['href'], 'wb') as x:
                x.write(obj.content)
        else:
            scrape(base + x['href'], URL)

scrape(base, '')
log.close()
