from bs4 import BeautifulSoup
import re
class Search():
    """Searching and confirmation of correct a part of source"""
    def __init__(self, name, soup):
        """Initialize method"""

        number = 0 
        L = ["a", "href", "class", "id", "a", " ", "p", "div", "span"]

        self.number = number
        self.name = name
        self.L = L
        self.soup = soup

    def search_content_name(self):
        self.number += 1
        #print(self.L[self.number])
        print(self.soup.find_all("a", string = re.compile("DOW")))
        if self.number > len(self.L) -1 :
            return self.search_content_name_by_href()
        return (self.soup.find_all(attrs={self.L[self.number]: self.name}), self.L[self.number])

    def search_content_name_by_href(self):
        return (self.soup.find_all(href = re.compile(self.name)), "href")

    