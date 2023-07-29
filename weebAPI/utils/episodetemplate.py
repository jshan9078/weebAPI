class Episode:
    def __init__(self, id, animeid, epNumber, snapshot, lang, duration, episodeLink):
        self.id = id 
        self.animeid = animeid 
        self.epNumber = epNumber
        self.snapshot = snapshot
        self.lang=lang
        self.duration=duration
        self.episodeLink = episodeLink

    def display(self):
        print(f"Episode {self.epNumber}")
        print(f"Language: {self.lang}")
        print(f"Duration: {self.duration}")
        print(f"Link: {self.episodeLink}")

    

