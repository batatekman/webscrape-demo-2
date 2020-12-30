import bs4
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

#headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}

# get url from target site
#url = 'http://www.newegg.com/p/pl?d=Graphics+cards&N=100006662'
url = 'http://www.hausples.com.pg/rent/?listing_type=lease&property_type=rental&order_by=relevance&is_certified=1&private_seller=1&q=location%3ANCD'

# open connection object and gets web page
req = Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'})
client_page = urlopen(req).read()
urlopen(req).close()

# parse obj_page using 'html_parser
soupPage = soup(client_page, "html.parser")

# get each container from site
containers = soupPage.findAll("div", {"class": "listing-card rental featured"})

print(soupPage.h1)
print(soupPage.p)

print("Containers: ", len(containers))

# Create CSV File
fileName = "rentals.csv"
f = open(fileName, "w")

# create headers for the data
csv_headers = "TITLE, CATEGORY, ADDRESS, PRICE\r\n"

f.write(csv_headers)

for container in containers:
    title = container.div.h2.text
    category_temp = container.findAll("div", {"class": "listing-category"})
    category = category_temp[0].text
    address_temp = container.findAll("div", {"class": "listing-address"})
    address = address_temp[0].text
    price_temp = container.findAll("div", {"class": "listing-price"})
    price = price_temp[0].text.strip()

    print("Title: " + title)
    print("Category: " + category)
    print("Address: " + address)
    print("Price: " + price)
    print("\r\n\r\n")

    f.write(title + "," + category.replace(",", "|") +
            "," + address.replace(",", "|") + "," + price.replace(",", "") + "\r\n")
