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


def rgb_from_hex(hex_color):
    hex_color = hex_color.replace("#", "")
    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)

    return dict(red=red, green=green, blue=blue)


def fetch_a_page_from_the_web(url_string):
    # get a file-like object form the page
    page = urllib.urlopen(url_string)
    page_content = page.read()

    # print page_content

    page.close()

    return page_content


def fetch_colors_info(page_content):
    soup = BeautifulSoup(page_content)

    # print soup.prettify()

    table = soup.find("table", "reference")
    trs = table.findChildren('tr')

    colors = []
    for tr in trs:
        tds = tr.findChildren('td')

        if len(tds) > 0:
            color_name = tds[0].find("a").string
            color_hex = tds[1].find("a").string

            color_dict = dict(name=color_name, components=rgb_from_hex(color_hex))

            colors.append(color_dict)

    print colors


url_string = "http://www.w3schools.com/cssref/css_colornames.asp"
page_content = fetch_a_page_from_the_web(url_string)
colors_info = fetch_colors_info(page_content)
