import sys
import requests
import os
homepage=os.path.expanduser('~')
subject = input("Enter wiki search:")
logname = (homepage+'/Desktop/logs')+'.txt'
try:
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
    try:
        file = open(logname,'a')
        if urlforlog:
            file.write(urlforlog+subject+"\n")
        
        file.close()

    except:
        print('Something went wrong! Cannot tell what?')
        sys.exit(0) 
except:
    file = open(logname,'a')
    file.write(("Tried to search for : "+subject+" not found\n"))
    print("An error occured")