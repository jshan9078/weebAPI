import os
from dotenv import load_dotenv
load_dotenv('.env')
playStem: str = os.getenv('PLAY_STEM')

class Anime:
    def __init__(self, id, title, type, epCount, status, season, year, score, poster, siteLink):
        self.id = id 
        self.title = title 
        self.type = type
        self.epCount = epCount 
        self.status = status 
        self.season = season
        self.year = year 
        self.score = score 
        self.poster = poster 
        self.siteLink = siteLink

    def optionDisplay(self):
        print(self.title)
        print(self.season,self.year)
        print(f"Episodes: {self.epCount}")
        print()

    def detailedDisplay(self):
        print(self.title)
        print("--------------")
        print(self.season,self.year)
        print(f"Status: {self.status}")
        print()
        print(f"Episodes: {self.epCount}")
        print()
        print(f"Poster Image: {self.poster}")
        print()
        print(f"Type: {self.type}")
        print()
        print(f"Score: {self.score}")
        print()
        print(f"Watch Link: {playStem}{self.siteLink}")
        print()

