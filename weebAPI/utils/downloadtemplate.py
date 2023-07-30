class Download:
    def __init__(self, url, res, fileSize, dub):
        self.url = url
        self.res = res 
        self.fileSize = fileSize 
        if (dub):
            self.dub = "Dub"
        else:
            self.dub = "Sub"
        self.downloadLink = None

    def display(self):
        print(self.dub)
        print(f"Resolution: {self.res}")
        print(f"Size: {self.fileSize}")
        if self.downloadLink!=None:
            print(f"Download Link: {self.downloadLink}")
        print()