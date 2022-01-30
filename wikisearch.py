import sys
import requests
import os
homepage=os.path.expanduser('~')
subject = input("Enter wiki search:")
url = 'https://en.wikipedia.org/w/api.php'
params = {
        'action': 'query',
        'format': 'json',
        'titles': subject,
        'prop': 'extracts',
        'exintro': True,
        'explaintext': True,
    }
 
response = requests.get(url, params=params)
data = response.json()

page = next(iter(data['query']['pages'].values()))
if page['extract']:
    print("Your search result")
    print(page['extract'])
    urlforlog="https://en.wikipedia.org/wiki/"
else:
    print("Nothing found in the wikipidea named",subject)


logname = (homepage+'/Desktop/logs')+'.txt'

try:
    file = open(logname,'a')
    if urlforlog:
        file.write(urlforlog+subject+"\n")
    else:
        file.write("Tried:",subject+"\n")
    file.close()

except:
    print('Something went wrong! Cannot tell what?')
    sys.exit(0) 