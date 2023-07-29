import requests
import re
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from decrypter import decrypt

def getDownloadOptions(session, targetEpisode):
    webpage = session.get(targetEpisode).text
    downloadOptions = re.findall('<a href="(?P<url>.+?)" .+? class="dropdown-item">.+? (?P<resolution>\d+)p.+?</a>',webpage)
    return downloadOptions


def getDownloadLink(session, downloadOptions, choice):
    intermediaryPageLink = downloadOptions[choice][0]
    intermediaryPage = session.get(intermediaryPageLink).text
    downloadPageLink = re.search('<a href="(.+?)" .+?>Redirect me</a>',intermediaryPage).group(1)
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




