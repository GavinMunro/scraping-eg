""" Scrape a particular Twitter account.
Gavin A.I. Munro
"""

import os
import time
from pathlib import Path

from bs4 import BeautifulSoup
from selenium import webdriver
from dotenv import load_dotenv


env_path = Path('.') / Path('.env')
load_dotenv(dotenv_path=str(env_path))
# The path to the local chromedriver executable should now be CHROMEDRIVER_PATH
chromedriver_path = os.getenv("CHROMEDRIVER_PATH")


def grab_html(url="https://twitter.com/BorisJohnson"):
    browser = webdriver.Chrome(executable_path=chromedriver_path)
    browser.get(url)
    time.sleep(5)
    html = browser.page_source
    soup = BeautifulSoup(html, "html5lib")
    browser.close()
    return soup


if __name__ == '__main__':
    parsed_html = grab_html()
    print(parsed_html)
