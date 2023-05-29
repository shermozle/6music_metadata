#!/usr/bin/python

import requests, json, re, time, urllib, os

host = os.getenv('HOST', '')
port = os.getenv('PORT', '')
user = os.getenv('USER', '')
password = os.getenv('PASSWORD', '')
mount = os.getenv('MOUNT', '')

sleep_timer = 10
while True:
    try:
        clients = requests.get('http://' + user + ':' + password + '@' + host + ':' + port + '/admin/listclients?mount=' + mount)
    except Exception as e:
        print("Error connecting to icecast: " + str(e))
    pattern = re.compile("<Listeners>0</Listeners>")
    searchResult = pattern.search(clients.text)
    if searchResult == None:
        print("We have a listener")
        getUrl = 'https://rms.api.bbc.co.uk/v2/services/bbc_6music/segments/latest'
        try:
            response = requests.get(getUrl)
        except Exception as e:
            print("Get url error: " + str(e))
        try:
            data = json.loads(response.text)
            metadata = data['data'][0]['titles']['primary'] + ' - ' + data['data'][0]['titles']['secondary']
            print(metadata)
        except Exception as e:
            print("Error:" + str(e))
            print(json.dumps(data))
        try:
            requests.get('http://' + user + ':' + password + '@' + host + ':' + port + '/admin/metadata.xsl?song=' + str(urllib.parse.quote(metadata)) + '&mount=' + urllib.parse.quote(mount) + '&mode=updinfo&charset=UTF-8')
            
        except Exception as e:
            print("Well that didn't work eh: " + str(e))
    else:
        print("Nobody listening")
    time.sleep(sleep_timer)
