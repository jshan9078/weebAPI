from fastapi import FastAPI
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from navigator.seriesfinder import getSearchResults, getEpisode, getFullData
from downloadmanager.downloadscraper import getDownloadLink, getDownloadOptions
from fastapi.middleware.cors import CORSMiddleware
session = requests.session()

app = FastAPI(title="weebAPI",description="A RESTful API made with FastAPI to scrape anime data from animepahe")

# origins = ["https://weebdachi.netlify.app","https://weebdachi.netlify.app/","https://weebdachi.netlify.app/search","https://weebdachi.netlify.app/view","https://weebdachi.netlify.app/index",
#            "weebdachi.netlify.app","weebdachi.netlify.app/","weebdachi.netlify.app/search","weebdachi.netlify.app/view","weebdachi.netlify.app/index",
#            "weebdachi.netlify.app/search/","weebdachi.netlify.app/view/","weebdachi.netlify.app/index/",
#            "https://weebdachi.netlify.app/search/","https://weebdachi.netlify.app/view/","https://weebdachi.netlify.app/index/"
#            ]

origins = ["https://weebdachi.netlify.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return "up and running"

@app.get('/get_search_results/{query}')
async def get_search_results(query: str):
    """Get search results by typing in the anime you are looking for"""

    return getSearchResults(session, query)

@app.get('/get_full_data/{siteLink}')
async def get_full_data(siteLink: str):
    """Get complete data for a specific anime by providing the siteLink. \n
    siteLink refers to the identifier following 'https://animepahe.ru/anime/' """

    return getFullData(session,siteLink)

@app.get('/get_episode/{siteLink}/{episodeNumber}')
async def get_episode(siteLink: str, episodeNumber: int):
    """Get data for a particular episode. \n
    siteLink refers to the identifier following 'https://animepahe.ru/anime/' """

    return getEpisode(session,siteLink,episodeNumber)

@app.get('/get_download_options/{episodeLink:path}')
async def get_download_options(episodeLink: str):
    """Get the available download options for a specific episode. \n
    episodeLink refers to the  complete 'https://animepahe.ru/play/' link for the episode"""
    return getDownloadOptions(session,episodeLink)

@app.get('/get_download_link/{intermediaryPageLink:path}')
async def get_download_link(intermediaryPageLink: str):
    """Get the link to the download file for a specific episode's download option \n
    intermediaryPageLink refers to the 'pahe.win' link """
    return getDownloadLink(session,intermediaryPageLink)



