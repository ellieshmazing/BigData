'''SCRAPER MODIFIED FROM TUTORIAL AT https://github.com/LearnDataSci/articles/blob/master/Ultimate%20Guide%20to%20Web%20Scraping/Part%201%20-%20Requests%20and%20BeautifulSoup/notebook.ipynb'''

#Input: Website HTML content and local path to save to
#Output: None
#Function to save HTML content locally
def saveHTML(content, outPath):
    with open(outPath, 'wb') as file:
        file.write(content)
        
#Input: Local path
#Output: Scraped website's HTML content
#Function to open locally stored HTML
def openHTML(inPath):
    with open(inPath, 'rb') as file:
        return file.read()
    
#Input: Local folder and URL
#Output: URL cleansed for use as filename
#Function to reformat URL as usable filename
def cleanseURL(path, URL):
    #Replace illegal filename characters with underscores
    cleanURL = URL.replace("/", "_").replace(":", "_")
    
    #Append filename to local folder and enforce length limit
    return path + cleanURL[:164]
    

import requests as req
from bs4 import BeautifulSoup as BS
from time import sleep

#Declare starting URL variables
baseURL = 'https://www.breitbart.com/politics/page/'
pageNum = 1

#Iterate through result pages until max reached (999)
while (pageNum < 1000):
    print(pageNum)
    #Download search result page
    search = req.get('{}{}'.format(baseURL, pageNum))

    #Save page content and open local copy
    saveHTML(search.content, f"../Articles/Breitbart/raw/search/{pageNum}")
    searchLocal = openHTML(f"../Articles/Breitbart/raw/search/{pageNum}")

    #Open search page as BS object using html parser
    searchSoup = BS(searchLocal, 'html.parser')
    
    #Declare array to hold article links from search page
    articleURLs = []

    #Gather all link objects under article tags on search page
    articleTags = searchSoup.select('article h2 a')

    #Extract URLs and place in array
    for count in range(len(articleTags)):
        articleURLs.append(articleTags[count]['href'])
    
    #Iterate through every article URL in link page
    for article in articleURLs:
        #Request article from link
        articleContent = req.get(article)
        
        #Format article URL for use as filename
        articleFile = cleanseURL("../Articles/Breitbart/raw/", article)
    
        #Save article locally
        saveHTML(articleContent.content, articleFile)
        '''articleLocal = openHTML(articleFile)
    
        #Open as BS object
        articleSoup = BS(articleLocal, 'html.parser')
    
        
        content = articleSoup.select(".entry-content p")
        print(content)'''
        
        #Sleep for a second
        sleep(1)
        
    #Increment search page
    pageNum += 1
    
    #Sleep for a second
    sleep(1)