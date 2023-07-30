from fastapi import FastAPI
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from navigator.seriesfinder import getSearchResults, getEpisode, getExtraData
from downloadmanager.downloadscraper import getDownloadLink, getDownloadOptions
session = requests.session()

app = FastAPI()

@app.get('/')
async def root():
    return "up and running"

@app.get('/get_search_results/{query}')
async def get_search_results(query: str):
    return getSearchResults(session, query)

@app.get('/get_episode/{siteSession}/{epCount}/{episodeNumber}')
async def get_episode(siteSession: str, epCount: int, episodeNumber: int):
    return getEpisode(session,epCount,siteSession,episodeNumber)

@app.get('/get_download_options/{episodeLink:path}')
async def get_download_options(episodeLink: str):
    return getDownloadOptions(session,episodeLink)

@app.get('/get_download_link/{intermediaryPageLink:path}')
async def get_download_link(intermediaryPageLink):
    return getDownloadLink(session,intermediaryPageLink)

@app.get('/get_extra_data/{fullSiteLink:path}')
async def get_extra_data(fullSiteLink):
    return getExtraData(session,fullSiteLink)



