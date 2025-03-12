# Scenario 1
import urllib.request,urllib.error
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

#Scenario 2
import urllib.request as ur, urllib.error as ue
try:
    with ur.urlopen('http://data.pr4e.org/romeo.txt') as response:
       
        print(response.getheader('Server'))
        print(response.getheader('content-type'))
except ue.URLError as e:
    print(f'Error fetching data: {e}') 

#Scenario 3
import urllib.request as ur, urllib.error as ue
try:
    with ur.urlopen('http://data.pr4e.org/romeo.txt') as response:
        data = response.read().decode()
        with open('local_romeo.txt','w') as file:
            file.write(data)
        print('Data has been written to local file')
except ue.URLError as e:
    print(f'Error parsing url: {e}')

#Scenario 4
import urllib.request as ur, urllib.error as ue
url = 'http://data.pr4e.org/cover3.jpg'
ur.urlretrieve(url,'cover.jpg')
print('Image saved')

#Scenario 5
import urllib.request as ur, urllib.error as ue
import time
url = "http://data.pr4e.org/romeo.txt"
start_time = time.time()
with ur.urlopen(url) as response:
    data = response.read().decode()
end_time = time.time()
print(f'Fetch completed in {end_time - start_time:.1f} seconds')