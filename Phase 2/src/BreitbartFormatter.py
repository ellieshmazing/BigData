'''Program to format HTML of Breitbart articles as text files that can be loaded into Hadoop'''

#Input: Local path
#Output: Scraped website's HTML content
#Function to open locally stored HTML
def openHTML(inPath):
    with open(inPath, 'rb') as file:
        return file.read()


import os
import json
from bs4 import BeautifulSoup as BS


#Declare array to hold all article objects
articleList = []

#Reformat directory path using os
articleDir = os.fsencode('../Articles/Breitbart/Raw/')

#Iterate through articles in directory
for articleFile in os.listdir(articleDir):
    #Convert back to string format
    articleFilename = os.fsdecode(articleFile)
    
    #Open HTML file, then convert to Soup object
    articleLocal = openHTML(articleFilename)
    articleSoup = BS(articleLocal, 'html.parser')
    
    articleAuthor = articleSoup.select_one('script meta[name="author"]').content
    articleTime = articleSoup.select_one('script meta[name="pubdate"]').content
    articleTitle = articleSoup.select_one('script meta[property="og:type"]').content
    articleContent = articleSoup.select('#MainW p')
    
    print(articleAuthor)
    print(articleTime)
    print(articleTitle)
    print(articleContent)