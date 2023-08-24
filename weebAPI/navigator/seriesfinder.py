import re
import os
import sys
import requests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.animetemplate import Anime
from utils.episodetemplate import Episode
session = requests.session()


def get_ddg_cookies(url):
    r = requests.get('https://check.ddos-guard.net/check.js', headers = {'referer': url})
    r.raise_for_status()
    return r.cookies.get_dict()['__ddg2']


def getSearchResults(session, query):
    my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
    session.headers.update(my_headers)
    url = f"https://animepahe.ru/api?m=search&q={query}"
    cookie = get_ddg_cookies(url)
    searchResults = []
    session.cookies.set(cookie,cookie,domain=url)
    searchResultsRaw = session.get(url).text
    return searchResultsRaw
    # seperated = re.findall('"id":(.+?),"title":"(.+?)","type":"(.+?)","episodes":(.+?),"status":"(.+?)","season":"(.+?)","year":(.+?),"score":(.+?),"poster":"(.+?)","session":"(.+?)"',searchResultsRaw)
    # for entry in seperated:
    #     parsedEntry = Anime(entry[1],entry[2],entry[4],entry[8],entry[9])
    #     searchResults.append(parsedEntry)
    # return searchResults

def getEpisode(session,siteLink,episodeNumber):
    my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
    session.headers.update(my_headers)
    counter=0
    i=1
    while True:
        try: 
            url = f"""{"https://animepahe.ru/api?m=release&id="}{siteLink}&sort=episode_asc&page={i}"""
            cookie = get_ddg_cookies(url)
            session.cookies.set(cookie,cookie,domain=url)
            episodeResultsRaw = session.get(url).text
            seperated = re.findall('"id":(.+?),"anime_id":(.+?),"episode":(.+?),"episode2":0,"edition":"","title":"","snapshot":"(.+?)","disc":"(.*?)","audio":"(.+?)","duration":"(.+?)","session":"(.+?)"',episodeResultsRaw)
            for entry in seperated:
                counter+=1
                if counter==episodeNumber:
                    newEpisodeObject = Episode(entry[0],entry[1],episodeNumber,entry[3],entry[5],entry[6],"https://animepahe.ru/play/"+siteLink+"/"+entry[7])
                    return newEpisodeObject
            i+=1
        except:
            return None
            
def getFullData(session, siteLink):
    my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
    session.headers.update(my_headers)
    fullSiteLink = "https://animepahe.ru/anime/"+siteLink
    cookie = get_ddg_cookies(fullSiteLink)
    session.cookies.set(cookie,cookie,domain=siteLink)
    rawdata = session.get(fullSiteLink).text
    category = re.findall('<a href="/anime/theme/(.+?)"',rawdata) + re.findall('<a href="/anime/genre/(.+?)"',rawdata) + re.findall('<a href="/anime/demographic/(.+?)"',rawdata)
    mal = re.findall('<a href="(.+?)" class="font-weight-bold" title.+?MyAnimeList"',rawdata)[0][2:]
    synopsis = re.findall('<div class="anime-synopsis">(.+?)</div>',rawdata)[0].replace('<br>','').replace('<i>','').replace('</i>','')
    id = int(re.findall('<meta name="id" content="(.+?)">',rawdata)[0])
    title = re.findall('<span class="sr-only unselectable">(.+?)</span>',rawdata)[0]
    type = re.findall('<a href="/anime/type/(.+?)"',rawdata)[0]
    url = f"""{"https://animepahe.ru/api?m=release&id="}{siteLink}&sort=episode_asc&page=1"""
    cookie = get_ddg_cookies(url)
    session.cookies.set(cookie,cookie,domain=url)
    episodeResultsRaw = session.get(url).text
    epCount = int(re.findall('"total":(.+?),',episodeResultsRaw)[0])
    epPages = int(re.findall('"last_page":(.+?),',episodeResultsRaw)[0])
    season = re.findall('<a href="/anime/season/.+?" title=".+?">(.+?)</a>',rawdata)[0]
    rawdata = ' '.join(rawdata.splitlines()).replace("\"",'')
    status = re.findall('Status: <a href=/anime/.+? title=(.+?)>',rawdata)[0]
    fullData = Anime(fullSiteLink=fullSiteLink,title=title,type=type,status=status,poster=None,siteLink=siteLink,id=id,epCount=epCount,season=season,category=category,mal=mal,synopsis=synopsis,epPages=epPages)
    return fullData





