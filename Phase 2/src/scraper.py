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
    
    #Append filename to local folder
    return path + cleanURL
    


import requests as req
from bs4 import BeautifulSoup as BS

url = 'https://www.breitbart.com/politics/page/2/'

r = req.get(url)

saveHTML(r.content, "../Articles/Breitbart/raw/search")
newR = openHTML("../Articles/Breitbart/raw/search")

soup = BS(newR, 'html.parser')
articleURLS = []


articleContent = soup.select('article h2 a')
print(articleContent)

for count in range(len(articleContent)):
    articleURLS.append(articleContent[count]['href'])
    
for article in articleURLS:
    r = req.get(article)
    cleanArticle = cleanseURL("../Articles/Breitbart/raw/", article)
    
    
    saveHTML(r.content, cleanArticle)
    newR = openHTML(cleanArticle)
    
    soup = BS(newR, 'html.parser')
    
    content = soup.select(".entry-content p")
    print(content)