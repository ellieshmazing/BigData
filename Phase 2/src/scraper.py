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
    


import requests as req
from bs4 import BeautifulSoup as BS

url = 'https://www.breitbart.com/politics/page/2/'

r = req.get(url)

saveHTML(r.content, "search")
newR = openHTML("search")

soup = BS(newR, 'html.parser')
articleURLS = []


articleContent = soup.select('article h2 a')
print(articleContent)

for count in range(len(articleContent)):
    articleURLS.append(articleContent[count]['href'])
    
print(articleURLS)
'''while(articleContent != None):
    articleContent = soup.select_one('article h2 a')['href']
    articleURLS.append(articleContent)
    print(articleContent)

print(articleURLS)'''