# import urllib.request, urllib.parse, urllib.error
# import json
# import xml.etree.ElementTree as et
# import ssl

# # Scenario 1
# url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_2168495.json').read()
# info = json.loads(url)
# comment_list = info['comments']
# counts = [int(stuff['count']) for stuff in comment_list]
# print('Sum of counts:', sum(counts))

# # Scenario 2
# url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_2168494.xml').read()
# stuff = et.fromstring(url)
# tree = stuff.findall('.//count')
# nums = [int(result.text) for result in tree]
# print('Sum of XML counts:', sum(nums))

# import urllib.request, urllib.parse, urllib.error
# import json, ssl

# # Scenario 3
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

# #Scenario 4
# import urllib.request as ur, urllib.error as ue
# import json
# try:
#     url = "http://py4e-data.dr-chuck.net/comments_2168495.json"
#     with ur.urlopen(url) as response:
#         data = response.read().decode()
#         info = json.loads(data)
#         counts = [item['count'] for item in info['comments']]
#         print(sum(counts))
# except ue.URLError as e:
#     print(f'Error parsing url: {e}')
# except json.JSONDecodeError as e:
#     print(f'Error parsing json: {e}')

# #Scenario 5
# import urllib.request as ur, urllib.error as ue
# import json
# url = 'http://py4e-data.dr-chuck.net/comments_2168495.json'
# with ur.urlopen(url) as response:
#     data = response.read().decode()
#     info = json.loads(data)
#     for comment in info['comments']:
#         if int(comment['count']) > 50:
#             print(comment['name'])

# #Scenario 6
# import urllib.request as ur, urllib.error as ue
# import json
# try:
#     url = "http://api.open-notify.org/astros.json"
#     with ur.urlopen(url) as response:
#         data = response.read().decode()
#         info = json.loads(data)
#         if info.get('message') == 'success':
#             print('Number of Astronauts:',info['number'])
#             if info['people']:
#                 print('First Astronaut:',info['people'][0]['name'])
# except ue.URLError as e:
#     print(f'Error parsing URL: {e}')
# except json.JSONDecodeError as e:
#     print(f'Error parsing json: {e}')

# #Scenario 7
# import urllib.request as ur, urllib.error as ue
# import json
# try:
#     url = 'https://api.open-meteo.com/v1/forecast?latitude=40.7128&longitude=-74.0060&current_weather=true'
#     with ur.urlopen(url) as response:
#         data = response.read().decode()
#         info = json.loads(data)
#         weather = info['current_weather']
#         temperature = weather['temperature']
#         weathercode = weather['weathercode']
#         if weathercode == 0:
#             condition = 'clear sky'
#         elif weathercode <= 3:
#             condition = 'cloudy'
#         else:
#             condition = 'other'
#         print(f'{temperature} degree celcius')
#         print(f'{condition}')
# except ue.URLError as e:
#     print(f'Error parsing url: {e}')
# except json.JSONDecodeError as e:
#     print(f'Error parsing JSON: {e}')
# except KeyError as e:
#     print(f'Error parsing JSON data: {e}')

#scenario 8
import urllib.request as ur, urllib.error as ue
import json
try:
    with ur.urlopen('https://randomuser.me/api/') as response:
        data = response.read().decode()
        info = json.loads(data)
        result = info['results'][0]
        title = result['name']['title']
        first_name = result['name']['first']
        last_name = result['name']['last']
        print(f'{title} {first_name} {last_name}')
        email = result['email']
        print(f'{email}')
except ue.URLError as e:
    print(f'Error parsing url: {e}')
except json.JSONDecodeError as e:
    print(f'Error parsing JSON: {e}')
except KeyError as e:
    print(f'Error parsing JSON data: {e}')
