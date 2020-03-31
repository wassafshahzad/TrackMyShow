from util.constants import MESSAGE, MESSAGE_HEAD
class User:
    
    def __init__(self, username,show):
        self.username = username
        self.show = show
        

    def notify(self,episode_number,toast,message):
        if (self.show.last_episode < episode_number):
            self.show.last_episode = str(episode_number)
            toast.show_toast(MESSAGE_HEAD, MESSAGE, duration=5)
