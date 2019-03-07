# BEATUFIL SOUP 4 testing
import urllib.request as ur
import queue
import threading
import time
import re
import win10toast
from bs4 import BeautifulSoup

queue = queue.Queue()
HDR = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

class Alert():
    """Class to create a single alert and getting operation on it"""

    def __init__(self, url):
        """ Initialize method"""
        self.url = url
        name_to_find = input("Type a name keyword to search")
        self.name_to_find = name_to_find

    def search_concent_name(self):
        soup = self.download_source()
        finds = soup.find_all(id = self.name_to_find)
        print(finds)

        decission = input("It's a good value for testing ? Y = yes N = now")
        if decission == 'y':
            self.finds = finds

    def download_source(self):
        req = ur.Request(self.url,headers= HDR)
        with ur.urlopen(req) as response:
            soup = BeautifulSoup(response.read(), 'html.parser')
        return soup

    def search_concent_changes_occurence(self):
        while True:

            source = self.download_source()
            check = source.find_all(id = self.name_to_find)
            self.check = check
            self.check_changes()
            time.sleep(0.5)

    def check_changes(self): 
        if queue.empty() == False:
            prev = queue.get()
            print(prev)
            if self.check != prev:     
                print("Changes")
                queue.put(self.check)
                #toaster = win10toast.ToastNotifier()
                #toaster.show_toast("Sample Notification from WebAlert","Concent has changed")
            else:
                print("stable")
        else:
            queue.put(self.check)

if __name__ == "__main__":
    print("Welcome on program to website content changes crawler | good to find very various things, for example: ratings, scores, pointers etc..")
    print("It's a test version and many features aren't available")
    print("Searching specific id's name only works")
    print("0 version")
    a = Alert("https://time.is/pl/")
    a.search_concent_name()

    thread1 = threading.Thread(target = a.search_concent_changes_occurence)

    thread1.start()
    thread1.join()