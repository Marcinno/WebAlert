# BEATUFIL SOUP 4 testing
import urllib.request as ur
import queue
import threading
import time
import re
import find_element
import win10toast
from bs4 import BeautifulSoup

#queue = queue.Queue()
HDR = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

class Alert():
    """Class to create a single alert and handling it"""

    def __init__(self, url):
        """ Initialize method"""
        
        downloaded_content_queue = queue.Queue()
        name_to_find = input("Type a name keyword to search")
        method_to_search_number = 0
        toaster = win10toast.ToastNotifier()

        self.downloaded_content_queue = downloaded_content_queue
        self.url = url
        self.name_to_find = name_to_find
        self.method_to_search_number = method_to_search_number
        self.toaster = toaster


    def prepare_searching_element(self):
        """searching a proper part of source"""
        answer = ""
        soup = self.download_source()
        #print(soup)
        search_object = find_element.Search(self.name_to_find, soup)
        while answer != "y": #temporary
            #print(soup)
            (suggest, value) = search_object.search_content_name()
            print(suggest)
            print("Good?")
            answer = input("It's a good value for testing ? y = yes n = now : ")

        self.find = suggest
        self.value = value
        self.search_concent_changes_occurence()

    def download_source(self):
        """Downloading source code"""
        req = ur.Request(self.url, headers = HDR)
        with ur.urlopen(req) as response:
            soup = BeautifulSoup(response.read(), 'html.parser')
        return soup

    def search_concent_changes_occurence(self):
        """Searching a code changes and comparision it"""
        while True:
            source = self.download_source()
            if self.value != "href":
                check = source.find_all(attrs={self.value : self.name_to_find})
            else:
                check = source.find_all(href = self.name_to_find)
            print("Check %r" %check)
            self.check = check
            self.check_changes()
            time.sleep(0.5)

    def check_changes(self): 
        """Checking two lastest version of soruce code"""
        if self.downloaded_content_queue.empty() == False:
            prev = self.downloaded_content_queue.get()
            #print(prev)
            if self.check != prev:     
                print("Changes")
                self.downloaded_content_queue.put(self.check)
                #self.toaster.show_toast("Sample Notification from WebAlert","Concent has changed") 
            else:
                print("stable")
        else:
            self.downloaded_content_queue.put(self.check)

if __name__ == "__main__":
    print("Welcome on program to website content changes crawler | good to find very various things, for example: ratings, scores, pointers etc..")
    print("It's a test version and many features aren't available")
    print("0.1 version")

    a = Alert("https://countryeconomy.com/stock-exchange")
    thread1 = threading.Thread(target = a.prepare_searching_element())

    thread1.start()
    thread1.join()