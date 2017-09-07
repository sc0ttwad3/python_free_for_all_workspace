from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup # as bs

# Grab graphics cards
# NewEgg Worksatation Graphics Cards
source_url = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709'

client = uReq(source_url) # open conn
# sauce =
page_html = client.read() # grab page
client.close() # close conn to be nice

# open file to create .csv of data
#   and write headers line
filename = "desktop-graphics-cards.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping\n"
f.write(headers)

# Parse the html
# soup =
page_soup = soup(page_html, "html.parser")




# traverse the graphics card page elements
containers = page_soup.body.findAll("div", {"class": "item-container"})

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

