# import urllib.request, urllib.parse, urllib.error
# import json, ssl

# # Example from the document
# serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# address = input('Enter location: ')
# parms = dict()
# parms['q'] = address.strip()
# url = serviceurl + urllib.parse.urlencode(parms)

# print('Retrieving', url)
# uh = urllib.request.urlopen(url, context=ctx)
# data = uh.read().decode()
# print('Retrieved', len(data), 'characters')
# try:
#     js = json.loads(data)
# except:
#     js = None
#     print('==== Failure To Parse JSON ====')
#     print(data)
#     quit()
# if not js or 'features' not in js:
#     print('==== Download error ===')
#     print(data)
#     quit()

# if len(js['features']) == 0:
#     print('==== Object not found ===')
#     print(data)
#     quit()

# plus_code = js['features'][0]['properties']['plus_code']
# print('Plus code', plus_code)

# # Additional web basics
# url = "http://data.pr4e.org/mbox.txt"
# try:
#     with urllib.request.urlopen(url) as response:
#         data = response.read().decode()
#         print("\nTotal characters:", len(data))
# except urllib.error.URLError as e:
#     print(f"Error: {e}")

# try:
#     with urllib.request.urlopen(url) as response:
#         print("Server:", response.getheader("Server"))
#         print("Content-Type:", response.getheader("Content-Type"))
# except urllib.error.URLError as e:
#     print(f"Error: {e}")

# #question 1
# import urllib.request as ur, urllib.error as ue
# try:
#     with ur.urlopen('http://data.pr4e.org/romeo.txt') as response:
       
#         print(response.getheader('Server'))
#         print(response.getheader('content-type'))
# except ue.URLError as e:
#     print(f'Error fetching data: {e}') 

#question 2
# import urllib.request as ur, urllib.error as ue
# try:
#     with ur.urlopen('http://data.pr4e.org/romeo.txt') as response:
#         data = response.read().decode()
#         with open('local_romeo.txt','w') as file:
#             file.write(data)
#         print('Data has been written to local file')
# except ue.URLError as e:
#     print(f'Error parsing url: {e}')


import urllib.request as ur, urllib.error as ue
import json
try:
    url = "http://py4e-data.dr-chuck.net/comments_2168495.json"
    with ur.urlopen(url) as response:
        data = response.read().decode()
        info = json.loads(data)
        counts = [item['count'] for item in info['comments']]
        print(sum(counts))
except ue.URLError as e:
    print(f'Error parsing url: {e}')
except json.JSONDecodeError as e:
    print(f'Error parsing json: {e}')