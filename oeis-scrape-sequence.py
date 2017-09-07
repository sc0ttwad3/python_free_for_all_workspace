from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs


# OEIS.org - Online Encylopedia of Integer Sequences
#
# Example URL using entry for:
#   1,2,3,6,11,23,47,106,235
#
sourceUrl = 'https://oeis.org/A000055'
sourceReq = uReq(sourceUrl) # open conn
pageHtml = sourceReq.read() # grab page
sourceReq.close() # close conn to be nice

# Parse the html
soup = bs(pageHtml, "html5lib")
# Alternate parser
#page_soup = soup(page_html, "html.parser")

# find the distinguishing tags and data for the sequence
seqId = soup.find('td', {'width': 100, 'valign': 'top', 'align': 'left'})
tdTags = soup.find_all('td', {'valign': 'top', 'align': 'left'})
seqDescription = ''

n = 0
for td in tdTags:
    if n == 1:
        rawText = td.text.strip()
        seqDescription = " ".join(rawText.split())

    n += 1

print('\nSequence Id: ', seqId.text.strip())
print('Description: ', seqDescription)


