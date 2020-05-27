import urllib.request
from bs4 import BeautifulSoup

class getArticle:
    def __init__(self, webPage):
        self.webPage = webPage

    def extract(self):
        content = urllib.request.urlopen(self.webPage)

        readPage = content.read
        soup = BeautifulSoup(readPage, 'html.parser')

        paragraphs = soup.find_all('p')

        return paragraphs

test = getArticle("http://example.com/")

test.extract()