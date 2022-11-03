import requests
from bs4 import BeautifulSoup
from datetime import datetime


url = "http://www.naver.net/"
response = requests.get(url)

# print(response.text[:500])

soup = BeautifulSoup(response.text, "html.parser") # get data
order = 1

# print(soup.title) # get title tag of html
# print(soup.title.string) # Convenience property to get the single string within this PageElement.
# print(soup.span) # find and return the first span tag
results = soup.findAll('a', "card_stock") # find all span tags

print(datetime.today().strftime("Stock news of %Y/%m/%d. \n"))

order_file = open("orderlist.txt","w")

for result in results:
    order_file.write( "list" + str(order) + result.get_text() + "\n")
    print("list", order,result.get_text(), "\n")
    order += 1


