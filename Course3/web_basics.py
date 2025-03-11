import urllib.request, urllib.parse, urllib.error
import json, ssl

# Example from the document
serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
parms = dict()
parms['q'] = address.strip()
url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
try:
    js = json.loads(data)
except:
    js = None
    print('==== Failure To Parse JSON ====')
    print(data)
    quit()
if not js or 'features' not in js:
    print('==== Download error ===')
    print(data)
    quit()

if len(js['features']) == 0:
    print('==== Object not found ===')
    print(data)
    quit()

plus_code = js['features'][0]['properties']['plus_code']
print('Plus code', plus_code)

# Additional web basics
url = "http://data.pr4e.org/mbox.txt"
try:
    with urllib.request.urlopen(url) as response:
        data = response.read().decode()
        print("\nTotal characters:", len(data))
except urllib.error.URLError as e:
    print(f"Error: {e}")

try:
    with urllib.request.urlopen(url) as response:
        print("Server:", response.getheader("Server"))
        print("Content-Type:", response.getheader("Content-Type"))
except urllib.error.URLError as e:
    print(f"Error: {e}")