class User:
    
    def __init__(self, username):
        self.username = username
        self.shows = {}

    def add_show(self,show):
        self.shows.append(show)