#!usr/bin/env python3

import pip._vendor.requests as requests, json

#obtain user's external IP address
ip = requests.get('https://api.ipify.org').content.decode('utf8')

#print IP address and some information about the IP address
def ipdata():
    ip = requests.get('https://api.ipify.org').content.decode('utf8')
    response = requests.get('http://ipwho.is/' + str(ip))
    json_response = response.json()
    print('Your External IP Address is: ', json_response['ip'])
    print('Your IP Type is: ', json_response['type'])
    print('Your Approximate Latitude is: ', json_response['latitude'])
    print('Your Approximate Longitude is: ', json_response['longitude'])