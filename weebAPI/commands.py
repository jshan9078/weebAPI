import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from navigator.seriesfinder import getSearchResults, getEpisode
from downloadmanager.downloadscraper import getDownloadLink, getDownloadOptions
session = requests.session()

def get_search_results(query):
    return getSearchResults(session, query)

def get_anime_link(result):
    return result.fullSiteLink

def get_episode(result, episodeNumber):
    return getEpisode(session,result,episodeNumber)

def get_episode_link(episode):
    return episode.episodeLink

def get_download_options(episodeLink):
    return getDownloadOptions(session,episodeLink)

def get_download_link(downloadOptions,choice):
    return getDownloadLink(session,downloadOptions,choice-1)

# r = get_search_results("jujutsu kaisen")[0]
# e = get_episode_link(get_episode(r,15))
# d = get_download_options(e)
# print(get_download_link(d,1))