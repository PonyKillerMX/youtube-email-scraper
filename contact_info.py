#!usr/bin/python 
# Project intended to get the email of creators from a youtube topic. 
# Input => Topic | Output => List of emails. 
from bs4 import BeautifulSoup, SoupStrainer
from link_scraper import LinkScraper
import requests
from urllib.request import Request, urlopen
import re

# this will return a list of 10 links on topic fornite 
fortnite = LinkScraper(10, "fortnite")
fortnite_links = fortnite.search()

req = Request(fortnite_links[0]) 
html_page = urlopen(req) 

soup = BeautifulSoup(html_page, "lxml")

links_page = []

for link in soup.findAll('a'): 
    links_page.append(link.get('href'))

print(links_page)

