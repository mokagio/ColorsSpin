# colors_spider.py
# A spider that fetches a color list from a web page and saves it in another format

"""
Things to do:
1. Fetch and html page from the internet
2. Parse it looking for the node that contains the colors list
3. Loop on the colors list child nodes generating a list of dictionaries with it
4. Save the list into a file using the proper formatting

Useful stuff found on
- http://www.boddie.org.uk/python/HTML.html
"""
import urllib
from bs4 import BeautifulSoup


def fetch_a_page_from_the_web(url_string):
    # get a file-like object form the page
    page = urllib.urlopen(url_string)
    page_content = page.read()

    # print page_content

    page.close()

    return page_content


def fetch_colors_info_node(page_content):
    soup = BeautifulSoup(page_content)
    print soup.prettify()


url_string = "http://www.w3schools.com/cssref/css_colornames.asp"
page_content = fetch_a_page_from_the_web(url_string)
colors_info = fetch_colors_info_node(page_content)
