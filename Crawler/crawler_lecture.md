# Crawler
---

- A software which collects data of website using crawler

```bash
pip install requests
```

# Request
---

There are some requests in request module such as PUT, GET, POST, DELETE.

```python
import requests

url = 'https://www.naver.com/'

response = requests.get(url)

print(response)

print(response.text)

print(response.url)

print(response.content)

print(response.encoding)

print(response.headers)

print(response.json)

print(response.links)

print(response.ok)

print(response.status_code)
```

After this, you will get ```<Response [200]>```which means success. 


# BeautifulSoap
---

```python
import requests
from bs4 import BeautifulSoup

url = "http://www.naver.com/"
response = requests.get(url)

# print(response.text[:500])

soup = BeautifulSoup(response.text, "html.parser") # get data

print(soup.title) # get title tag of html
print(soup.title.string) # Convenience property to get the single string within this PageElement.
print(soup.span) # find and return the first span tag
print(soup.findAll('span')) # find all span tags

```

- What is beautifulSoap?     
- Python library that is used for web scraping purposes to pull the data out of HTML and XML files.

# Write results in a file
---

```python

order_file = open("orderlist.txt","w")

for result in results:
    order_file.write( "list" + str(order) + result.get_text() + "\n")
    print("list", order,result.get_text(), "\n")
    order += 1
```

