import re
import os
import sys
import requests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from decrypter import decrypt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.downloadtemplate import Download
session = requests.session()

def get_ddg_cookies(url):
    r = requests.get('https://check.ddos-guard.net/check.js', headers = {'referer': url})
    r.raise_for_status()
    return r.cookies.get_dict()['__ddg2']

def getDownloadOptions(session, targetEpisode):
    my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    session.headers.update(my_headers)
    cookie = get_ddg_cookies(targetEpisode)
    session.cookies.set(cookie,cookie,domain=targetEpisode)
    webpage = session.get(targetEpisode).text
    rawDownloadOptions = re.findall('<a href="(?P<url>.+?)" .+? class="dropdown-item">.+? (?P<resolution>\d+)p (.+?)MB(.+?)</a>',webpage)
    downloadOptions=[]
    for option in rawDownloadOptions:
        url = option[0]
        resolution = option[1]+"p"
        fileSize = option[2][1:] + "MB"
        dub = "eng" in option[3]
        downloadOption = Download(url,resolution,fileSize,dub)
        downloadOptions.append(downloadOption)
    return downloadOptions


def getDownloadLink(session, intermediaryPageLink):
    my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    session.headers.update(my_headers)
    cookie = get_ddg_cookies(intermediaryPageLink)
    session.cookies.set(cookie,cookie,domain=intermediaryPageLink)
    intermediaryPage = session.get(intermediaryPageLink).text
    downloadPageLink = re.search('<a href="(.+?)" .+?>Redirect me</a>',intermediaryPage).group(1)
    cookie = get_ddg_cookies(downloadPageLink)
    session.cookies.set(cookie,cookie,domain=downloadPageLink)
    downloadPage = session.get(downloadPageLink).text
    full_key, key, v1, v2 = re.search('\("(\w+)",\d+,"(\w+)",(\d+),(\d+),\d+\)',downloadPage).group(1,2,3,4)
    decrypted = decrypt(full_key,key,v1,v2)
    content = session.post(
        re.search('action="(.+?)"',decrypted).group(1),
        allow_redirects=False,
        data={"_token":re.search('value="(.+?)"',decrypted).group(1)},
        headers={"Referer": "https://kwik.cx/",},
        )
    return content.headers["Location"]

