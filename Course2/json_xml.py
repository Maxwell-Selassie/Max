import urllib.request, urllib.parse, urllib.error
import json
import xml.etree.ElementTree as et
import ssl

# JSON example
url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_2168495.json').read()
info = json.loads(url)
comment_list = info['comments']
counts = [int(stuff['count']) for stuff in comment_list]
print('Sum of counts:', sum(counts))

# XML example
url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_2168494.xml').read()
stuff = et.fromstring(url)
tree = stuff.findall('.//count')
nums = [int(result.text) for result in tree]
print('Sum of XML counts:', sum(nums))