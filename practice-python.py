import string 
import requests 
from bs4 import BeautifulSoup 


class Profile: 
    """Target the profile of individual people"""
    def __init__(self, region, name): 
        self.region = region 
        self.name = name 

    def get_region(self): 
        return self.region 

    def get_name(self): 
        return self.name

    def region_and_name(self): 
        return (self.name + self.region)


emilio = Profile("Mexico", "emilio")
print(emilio.region_and_name())
print(emilio.get_name())
print(emilio.get.region())
















