import requests
import numpy as np
import requests
from urllib.parse import urlencode

Serviceurl ='https://maps.googleapis.com/maps/api/geocode/json?'
Serviceurl1 ='https://maps.googleapis.com/maps/api/distancematrix/json?'
apikey = "AIzaSyDU0htGljNxQhrJ8BimYV7OMml31IrHrOo"
response = []
address = 'תל אביב'

with open('dests.txt', "r", encoding="utf8") as f:
    cities = [line.rstrip('\n') for line in f]

for c in cities:
    parms= {}
    parms1={}
    parms['origins'] = 'תל אביב'
    parms['destinations'] = c
    parms['key'] = apikey
    url= Serviceurl1 + urlencode(parms)
    response.append(requests.get(url).json())

    parms1['address']= c
    parms1['key'] = apikey
    url1 = Serviceurl + urlencode(parms1)
    response.append(requests.get(url1).json())


dis = []
i=0
j=1
dict = {}
for city in response:
    addresses = response[i]['destination_addresses'][0]
    dict[addresses] = {'distance': "" , 'time': ""}
    dict[addresses]['distance'] = response[i]['rows'][0]['elements'][0]['distance']['text']
    dict[addresses]['time'] = response[i]['rows'][0]['elements'][0]['duration']['text']
    dict[addresses]['longitude'] = response[j]['results'][0]['geometry']['location']['lng']
    dict[addresses]['latitude'] = response[j]['results'][0]['geometry']['location']['lat']
    dis.append(response[i]['rows'][0]['elements'][0]['distance']['value'])
    print('(', addresses, ')', ',' 'distance:', dict[addresses]['distance'], ',' 'time:', dict[addresses]['time'], ',' 'longitude:',
          dict[addresses]['longitude'], ',' 'latitude:', dict[addresses]['latitude'])
    i = i+2
    j = j+2
    if i>8 and j>9:
        break

import numpy as np
sort_dis = np.argsort(dis)[2:]
most_far_cities = []
list1 = list(dict.keys())

print("The most far cities from Tel-Aviv, Israel:")
for i in sort_dis:
    most_far_cities.append(list1[i])
    print(list1[i])
