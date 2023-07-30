import re
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from decrypter import decrypt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.downloadtemplate import Download


def getDownloadOptions(session, targetEpisode):
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




