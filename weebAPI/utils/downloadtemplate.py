class Download:
    def __init__(self, url, res, fileSize, type):
        self.url = url
        self.res = res 
        self.fileSize = fileSize 
        if (type):
            self.type = "Dub"
        else:
            self.type = "Sub"
        self.downloadLink = None

    def display(self):
        print(self.type)
        print(f"Resolution: {self.res}")
        print(f"Size: {self.fileSize}")
        if self.downloadLink!=None:
            print(f"Download Link: {self.downloadLink}")
        print()