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


def twitter_page(handle="BorisJohnson"):
    """ Use webdriver with Chrome as the browser/driver to grab the HTML page
    rendered by React on Twitter and parse that with html5lib to get Beautiful Soup.
    """
    base_url = "https://twitter.com"
    url = base_url + "/" + handle
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument("--disable-dev-shm-using")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=chrome_options)
    
    browser.get(url)
    time.sleep(3)  # wait = WebDriverWait(driver, 5)
    html = browser.page_source
    soup = BeautifulSoup(html, "html5lib")
    browser.close()
    return soup


def check_tweets(handle, tweets):
    """ Extract the text of the last 5 tweets in the Beautiful Soup object. """
    parsed_html = twitter_page(handle)
    html_els = parsed_html.find_all(lang="en")
    # Currently Twitter seems to use a lang=?? attribute only in the parent div of the tweet text.
    if not tweets:
        tweets = []
    for el in html_els:
        tweet_text = el.string
        if tweet_text:  # Only the first 5 HTML elements found have a string but that's all we need.
            if tweet_text not in tweets:
                print(tweet_text)
                tweets.append(tweet_text)
    return tweets
