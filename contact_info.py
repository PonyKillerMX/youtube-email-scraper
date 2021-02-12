#!usr/bin/python 
# Project intended to get the email of creators from a youtube topic. 
# Input => Topic | Output => List of emails. 
from bs4 import BeautifulSoup, SoupStrainer
from link_scraper import LinkScraper
import requests
import pprint as pp
import httplib2


# this will return a list of 10 links on topic fornite 
fortnite = LinkScraper(10, "fortnite")
fortnite_links = fortnite.search()

http = httplib2.Http()
status, response = http.request(url)
    #iterate through links and get contact info.  
    # for url in links[0]: 
   for url in links:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")

def print




















