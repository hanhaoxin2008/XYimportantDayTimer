class Timer:
    def __init__(self,id,name,datetime):
        self.id = id
        self.name = name
        self.datetime = datetime
    def getName(self):
        return self.name
    def getDatetime(self):
        return self.datetime