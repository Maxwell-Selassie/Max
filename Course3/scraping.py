#Scenario 1
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def web_crawler(url):
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.URLError as error:
        print(f'Error accessing URL: {error}')
        return 0
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('span')
    total = 0
    for tag in tags:
        if tag.get('class') == ['comments']:
            number = int(tag.contents[0])
            total += number
    return total
print(web_crawler(input('Enter: ')))

#Scenario 2
import urllib.request as ur, urllib.error as ue
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/Information_system'
with ur.urlopen(url) as response:
    data = response.read().decode()
    soup = BeautifulSoup(data,'html.parser')
    tags = soup('a')
    for tag in tags:
        print(tag.get_text().strip())

