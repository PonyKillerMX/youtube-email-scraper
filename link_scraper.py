#!usr/bin/python 
# Project intended to get the email of creators from a youtube topic. 
# Input => Topic | Output => List of emails. 

from youtubesearchpython import * 

class LinkScraper: 
    def __init__(self, limit, topic): 
        self.limit = limit
        self.topic = topic

    def search(self): 
        self.links = []
        # first parameter is title
        self.allsearch = Search("Fortnite", limit=self.limit, region="US")

        self.result_search = self.allsearch.result()
        #search for links
        for i in range(self.limit): 
            self.complete_result = self.result_search.get('result')[i]
            self.link = self.complete_result.get('link')
            # add the link to my list 
            self.links.append(self.link) 
        
        # return the final list of links 
        return (self.links) 



















