import requests
import re
from dotenv import load_dotenv
import os
import sys
import math
load_dotenv('.env')
searchStem: str = os.getenv('SEARCH_STEM')
episodeStem: str=os.getenv('EPISODE_STEM')
playStem: str = os.getenv('PLAY_STEM')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.animetemplate import Anime
from utils.episodetemplate import Episode

def getSearchResults(session, query):
    searchResults = []
    searchResultsRaw = session.get(searchStem+query).text
    seperated = re.findall('"id":(.+?),"title":"(.+?)","type":"(.+?)","episodes":(.+?),"status":"(.+?)","season":"(.+?)","year":(.+?),"score":(.+?),"poster":"(.+?)","session":"(.+?)"',searchResultsRaw)
    for entry in seperated:
        parsedEntry = Anime(entry[0],entry[1],entry[2],entry[3],entry[4],entry[5],entry[6],entry[7],entry[8],entry[9])
        searchResults.append(parsedEntry)
    return searchResults

def getEpisode(session,result,episodeNumber):
    pageCount=math.ceil(int(result.epCount)/30)
    for i in range(1,pageCount+1,1):
        episodeResultsRaw = session.get(f"""{episodeStem}{result.siteLink}&sort=episode_asc&page={i}""").text
        seperated = re.findall('"id":(.+?),"anime_id":(.+?),"episode":(.+?),"episode2":0,"edition":"","title":"","snapshot":"(.+?)","disc":"(.*?)","audio":"(.+?)","duration":"(.+?)","session":"(.+?)"',episodeResultsRaw)
        for entry in seperated:
            if int(entry[2])==episodeNumber:
                newEpisodeObject = Episode(entry[0],entry[1],entry[2],entry[3],entry[5],entry[6],playStem+result.siteLink+"/"+entry[7])
                return newEpisodeObject
            

            
        








