from fastapi import FastAPI
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from navigator.seriesfinder import getSearchResults, getEpisode, getFullData
from downloadmanager.downloadscraper import getDownloadLink, getDownloadOptions
session = requests.session()

app = FastAPI()

@app.get('/')
async def root():
    return "up and running"

@app.get('/get_search_results/{query}')
async def get_search_results(query: str):
    return getSearchResults(session, query)

@app.get('/get_full_data/{siteLink}')
async def get_full_data(siteLink):
    return getFullData(session,siteLink)

@app.get('/get_episode/{siteLink}/{epPages}/{episodeNumber}')
async def get_episode(siteLink: str, epPages: int, episodeNumber: int):
    return getEpisode(session,epPages,siteLink,episodeNumber)

@app.get('/get_download_options/{episodeLink:path}')
async def get_download_options(episodeLink: str):
    return getDownloadOptions(session,episodeLink)

@app.get('/get_download_link/{intermediaryPageLink:path}')
async def get_download_link(intermediaryPageLink):
    return getDownloadLink(session,intermediaryPageLink)



