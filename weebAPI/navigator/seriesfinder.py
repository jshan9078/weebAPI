import requests
import re
from dotenv import load_dotenv
import os
import sys
load_dotenv('.env')
searchStem: str = os.getenv('SEARCH_STEM')
playStem: str = os.getenv('PLAY_STEM')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.animetemplate import Anime

session = requests.session()


def getSearchResults(session, query):
    searchResults = []
    searchResultsRaw = session.get(searchStem+query).text
    seperated = re.findall('"id":(.+?),"title":"(.+?)","type":"(.+?)","episodes":(.+?),"status":"(.+?)","season":"(.+?)","year":(.+?),"score":(.+?),"poster":"(.+?)","session":"(.+?)"',searchResultsRaw)
    for entry in seperated:
        siteLink = playStem+entry[9]
        parsedEntry = Anime(entry[0],entry[1],entry[2],entry[3],entry[4],entry[5],entry[6],entry[7],entry[8],siteLink)
        searchResults.append(parsedEntry)
    return searchResults





