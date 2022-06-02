from selenium import webdriver
import time # for sleep()
import datetime # for now()
import pytz # for timezone()
import requests
from bs4 import BeautifulSoup
import re

browser=webdriver.Chrome("C:\\Users\\karta\\OneDrive\\Masaüstü\\chromedriver.exe",9515)
repo_url="https://github.com/facebook/flow"

browser.get(repo_url)
time.sleep(4)
html = browser.page_source
starstring='users starred this repository'
#string2="users starred this repository\" data-singular-suffix=\"user starred this repository"
index1=html.index(starstring)
#index2=html.index(string2)
stringg=html[index1-10:index1-1]
empty_str=""
for i in stringg:
    if(i in ['0','1','2','3','4','5','6','7','8','9']):
        empty_str+=i
print(f"\nAs of {datetime.datetime.now(pytz.timezone('Europe/Istanbul'))}, {empty_str} users starred this repository.")
time.sleep(2)

browser.get(repo_url+'/issues')
time.sleep(4)
html = browser.page_source
openissuesstring="""Open
    </a>"""
closedissuesstring="""Closed
    </a>"""
index2=html.index(openissuesstring)
index3=html.index(closedissuesstring)
stringg=html[index2-10:index2-1].strip()
stringg2=html[index3-10:index3-1].strip()
print(f"As of {datetime.datetime.now(pytz.timezone('Europe/Istanbul'))}, {stringg} Open Issues.")
print(f"As of {datetime.datetime.now(pytz.timezone('Europe/Istanbul'))}, {stringg2} Closed Issues.")
time.sleep(2)

browser.get(repo_url+'/pulls')
time.sleep(4)
html = browser.page_source
openissuesstring="""Open
    </a>"""
closedissuesstring="""Closed
    </a>"""
index2=html.index(openissuesstring)
index3=html.index(closedissuesstring)
stringg=html[index2-10:index2-1].strip()
stringg2=html[index3-10:index3-1].strip()
print(f"As of {datetime.datetime.now(pytz.timezone('Europe/Istanbul'))}, {stringg} Open PRs.")
print(f"As of {datetime.datetime.now(pytz.timezone('Europe/Istanbul'))}, {stringg2} Closed PRs.")
time.sleep(10)

browser.close() # closing the web browser