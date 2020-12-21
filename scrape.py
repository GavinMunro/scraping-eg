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
    """ Use webdriver with Chrome as the browser/driver to grab the HTML
    rendered by React and parse that with html5lib to get soup object.
    """
    browser = webdriver.Chrome(executable_path=chromedriver_path)
    browser.get(url)
    time.sleep(3)  # wait = WebDriverWait(driver, 5)
    html = browser.page_source
    soup = BeautifulSoup(html, "html5lib")
    browser.close()
    return soup


if __name__ == '__main__':
    parsed_html = grab_html()
    html_els = parsed_html.find_all(lang="en")
    # Currently Twitter seems to use a lang=?? attribute only in the parent div of the tweet text.
    tweets = []
    for el in html_els:
        tweet_text = el.string
        if tweet_text:  # Only the first 5 HTML elements found have a string but that's all we need.
            tweets.append(tweet_text)
    print(tweets)
