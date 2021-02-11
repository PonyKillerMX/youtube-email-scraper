#!usr/bin/python 
# Project intended to get the email of creators from a youtube topic. 
# Input => Topic | Output => List of emails. 

from youtubesearchpython import * 

limit = 10 
# first parameter is title
allsearch = Search("Fortnite", limit=limit, region="US")

result_search = allsearch.result()
#search for links
for i in range(limit): 
    complete_result = result_search.get('result')[i]
    link = complete_result.get('link')
    print(link)






















