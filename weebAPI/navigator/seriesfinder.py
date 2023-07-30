import requests
import re
import os
import sys
import math
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.animetemplate import Anime
from utils.episodetemplate import Episode

def getSearchResults(session, query):
    searchResults = []
    searchResultsRaw = session.get("https://animepahe.ru/api?m=search&q="+query).text
    seperated = re.findall('"id":(.+?),"title":"(.+?)","type":"(.+?)","episodes":(.+?),"status":"(.+?)","season":"(.+?)","year":(.+?),"score":(.+?),"poster":"(.+?)","session":"(.+?)"',searchResultsRaw)
    for entry in seperated:
        parsedEntry = Anime(entry[1],entry[2],entry[4],entry[8],entry[9])
        searchResults.append(parsedEntry)
    return searchResults

def getEpisode(session,epPages,siteLink,episodeNumber):
    counter=0
    for i in range(1,epPages+1,1):
        episodeResultsRaw = session.get(f"""{"https://animepahe.ru/api?m=release&id="}{siteLink}&sort=episode_asc&page={i}""").text
        seperated = re.findall('"id":(.+?),"anime_id":(.+?),"episode":(.+?),"episode2":0,"edition":"","title":"","snapshot":"(.+?)","disc":"(.*?)","audio":"(.+?)","duration":"(.+?)","session":"(.+?)"',episodeResultsRaw)
        for entry in seperated:
            counter+=1
            if counter==episodeNumber:
                newEpisodeObject = Episode(entry[0],entry[1],episodeNumber,entry[3],entry[5],entry[6],"https://animepahe.ru/play/"+siteLink+"/"+entry[7])
                return newEpisodeObject
            
def getFullData(session, siteLink):
    fullSiteLink = "https://animepahe.ru/anime/"+siteLink
    rawdata = session.get(fullSiteLink).text
    category = re.findall('<a href="/anime/theme/(.+?)"',rawdata) + re.findall('<a href="/anime/genre/(.+?)"',rawdata) + re.findall('<a href="/anime/demographic/(.+?)"',rawdata)
    mal = re.findall('<a href="(.+?)" class="font-weight-bold" title=".+? on MyAnimeList"',rawdata)[0]
    synopsis = re.findall('<div class="anime-synopsis">(.+?)</div>',rawdata)[0].replace('<br>','').replace('<i>','').replace('</i>','')
    id = int(re.findall('<meta name="id" content="(.+?)">',rawdata)[0])
    title = re.findall('<span class="sr-only unselectable">(.+?)</span>',rawdata)[0]
    type = re.findall('<a href="/anime/type/(.+?)"',rawdata)[0]
    episodeResultsRaw = session.get(f"""{"https://animepahe.ru/api?m=release&id="}{siteLink}&sort=episode_asc&page=1""").text
    epCount = int(re.findall('"total":(.+?),',episodeResultsRaw)[0])
    epPages = int(re.findall('"last_page":(.+?),',episodeResultsRaw)[0])
    season = re.findall('<a href="/anime/season/.+?" title=".+?">(.+?)</a>',rawdata)[0]
    poster = re.findall('<a href="(.+?)" class="youtube-preview">',rawdata)[0]
    rawdata = ' '.join(rawdata.splitlines()).replace("\"",'')
    status = re.findall('Status: <a href=/anime/.+? title=(.+?)>',rawdata)[0]
    fullData = Anime(fullSiteLink=fullSiteLink,title=title,type=type,status=status,poster=poster,siteLink=siteLink,id=id,epCount=epCount,season=season,category=category,mal=mal,synopsis=synopsis,epPages=epPages)
    return fullData


        








