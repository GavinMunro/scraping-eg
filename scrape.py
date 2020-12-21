""" Scrape a particular Twitter account.
Gavin A.I. Munro
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen


def grab_html(url="https://twitter.com"):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parse")
    return soup


if __name__ == '__main__':
    parsed_html = grab_html()
    print(parsed_html)
