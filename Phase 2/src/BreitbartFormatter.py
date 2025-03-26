'''Program to format HTML of Breitbart articles as text files that can be loaded into Hadoop'''

#Input: Local path
#Output: Scraped website's HTML content
#Function to open locally stored HTML
def openHTML(inPath):
    with open(inPath, 'rb') as file:
        return file.read()
    
#Input: Array of SoupTags
#Output: Content cleansed as single string without HTML tags
#Function to cleanse paragraph array
def cleanseArticleContent(articleContent):
    #Declare base string to hold article
    articleContentPlain = ""
    
    #Iterate through all paragraph tags and append to the end of string
    for i in range(len(articleContent)):
        articleContentPlain = articleContentPlain + articleContent[i].get_text()
        
    #Return concatenated article
    return articleContentPlain

import os
import json
from bs4 import BeautifulSoup as BS


#Declare array to hold all article objects
articleList = []

#Reformat directory path using os
baseDir = '../Articles/Breitbart/Raw/'
articleDir = os.fsencode(baseDir)

#Iterate through articles in directory
for articleFile in os.listdir(articleDir):
    #Convert back to string format
    articleFilename = os.fsdecode(articleFile)
    
    #Open HTML file, then convert to Soup object
    articleLocal = openHTML(baseDir + articleFilename)
    articleSoup = BS(articleLocal, 'html.parser')
    
    #Extract necessary meta information
    articleAuthor = articleSoup.select_one('meta[name="author"]')['content']
    articleTime = articleSoup.select_one('meta[name="pubdate"]')['content']
    articleTitle = articleSoup.select_one('meta[property="og:title"]')['content']
    
    #Extract and format article contents
    articleContent = articleSoup.select('#MainW p')
    articleContentFormatted = cleanseArticleContent(articleContent)
    
    #Declare dictionary to hold article
    article = {
        "Title": articleTitle,
        "Time": articleTime,
        "Author": articleAuthor,
        "Content": articleContentFormatted
    }
    
    #Append article to list
    articleList.append(article)
    
with open("../Articles/Breitbart/Extracted/articles.json", "w") as f:
    json.dump(articleList, f)