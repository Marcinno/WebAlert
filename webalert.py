# BEATUFIL SOUP 4 testing
import urllib.request as ur
import queue
import threading
import time
import re
from bs4 import BeautifulSoup
#####################

queue = queue.Queue()
HDR = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def search(l):
    req = ur.Request(l, headers=HDR)
    with ur.lopen(req) as response:
        soup = BeautifulSoup(response.read(), 'html.parser')
        # print(soup)

    name = input("Type name to handling")

    finds = soup.find_all(name)
    print(finds)
    check_changes(finds)

def check_changes(finds):
    if queue.empty() == False:
        prev = queue.get()
        if finds != prev:     
            print("Changes")
            queue.put(finds)
        else:
            print("stable")
    else:
        queue.put(finds)

if __name__ == "__main__":
    print("Welcome on program to website content changes crawler | good to find very various things, for example: ratings, scores, pointers etc..")
    print("It's a test version and many features aren't available")
    print("Searching specific id's name only works")
    print("0 version")

    while True:
         search("http://api.nbp.pl/api/cenyzlota")
         time.sleep(3)
   


#print(soce)

#soup = BeautifulSoup(l, 'html.parser')

#print(soup.prettify()) # method to change compressed file to uncompressed tree format

#print(soup.find_all(id = "twd"))