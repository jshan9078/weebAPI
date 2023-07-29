# import requests
# import re
# from dotenv import load_dotenv
# import os
# from weeb-api.utils.animetemplate import Anime

# load_dotenv('.env')
# searchStem: str = os.getenv('SEARCH_STEM')
# session = requests.session()


# def getSearchResults(session, query):
#     searchResults = []
#     searchResultsRaw = session.get(searchStem+query).text
#     seperated = re.findall('"id":(.+?),"title":"(.+?)","type":"(.+?)","episodes":(.+?),"status":"(.+?)","season":"(.+?)","year":(.+?),"score":(.+?),"poster":"(.+?)","session":"(.+?)"',searchResultsRaw)
    
#     for entry in seperated:
#         #parsedEntry = Anime(entry[0],entry[1],entry[2],entry[3],entry[4],entry[5],entry[6],entry[7],entry[8],entry[9])
#         searchResults.append(parsedEntry)
#     return searchResults



