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

    return colors


def lower_case_first_letter_of_string(string):
    first_letter = string[0]
    return first_letter.lower() + string[1:]


def format_color_component(component):
    return "%.3f" % float(float(component) / 255)


def method_definition_string(color):
    return "+ (UIColor *)" + lower_case_first_letter_of_string(color['name']) + "Color;"


def method_implementation_string(color):
    red = color['components']['red']
    green = color['components']['green']
    blue = color['components']['blue']

    implementation = "+ (UIColor *)" + lower_case_first_letter_of_string(color['name']) + "Color"
    implementation = implementation + "\n{"

    implementation = implementation + "\n"

    implementation = implementation + "\t// " + color['name']
    implementation = implementation + " - " + str(red) + " "
    implementation = implementation + str(green) + " "
    implementation = implementation + str(blue)

    implementation = implementation + "\n"

    implementation = implementation + "\treturn [UIColor colorWithRed:"
    implementation = implementation + format_color_component(red)
    implementation = implementation + " green:" + format_color_component(green)
    implementation = implementation + " blue:" + format_color_component(blue)
    implementation = implementation + "];"

    implementation = implementation + "\n}"

    return implementation


def format_colors_for_objective_c(colors):
    for color in colors:
        print method_definition_string(color)
        print method_implementation_string(color)
        print "-" * 8


url_string = "http://www.w3schools.com/cssref/css_colornames.asp"
page_content = fetch_a_page_from_the_web(url_string)
colors_info = fetch_colors_info(page_content)
formatted_colors = format_colors_for_objective_c(colors_info)
