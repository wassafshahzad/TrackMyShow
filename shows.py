from util.validator import null_validation,link_validator,episode_validator
from util.constants import TEST_STRING
class Show:
    def __init__(self, link, last_episode):
        self.link = link
        self.last_episode = last_episode

    @property
    def link(self):
        return self._link
   
    @link.setter
    @null_validation
    @link_validator
    def link(self,link):
        self._link = link
    
    @property
    def last_episode(self):
        return self._last_episode
    
    @last_episode.setter
    @null_validation
    @episode_validator
    def last_episode(self,last_episode):
        self._last_episode = int(last_episode)
