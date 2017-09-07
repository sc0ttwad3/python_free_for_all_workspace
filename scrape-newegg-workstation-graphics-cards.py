from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# Grab graphics cards
# NewEgg Worksatation Graphics Cards
source_url = 'https://www.newegg.com/Workstation-Graphics-Cards/SubCategory/ID-449?Tid=8333'

client = uReq(source_url) # open conn
page_html = client.read() # grab page
client.close() # close conn to be nice

# Parse the html
page_soup = soup(page_html, "html.parser")
# print(page_soup.h1) # print Page Title H1

# open file to create .csv of data
filename = "workstation-graphics-cards.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"
f.write(headers)

# traverse the graphics card page elements
containers = page_soup.findAll("div", {"class": "item-container"})
how_many_cards = len(containers)


for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class": "item-title"})
    title = title_container[0].text.replace(",", "|")

    ship_container = container.findAll("li", {"class": "price-ship"})
    ship = ship_container[0].text.strip() # remove newlines, etc.

    print(brand)
    print(title)
    print(ship)

    f.write(brand + "," + title + "," + ship + "\n")

f.close()

# print('\nNumber of graphics cards:')
# print(len(containers))


