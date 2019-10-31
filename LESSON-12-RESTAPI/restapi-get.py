import json
import requests
import urllib.request
# urllib.request is used to grab the proxy information from system to use it in the request.
# set in env by 'export https_proxy=123.456.0.1:8080'

parameters = {
    "date_time": '2019-09-26T12:00:00'
}
response = requests.get('https://api.data.gov.sg/v1/environment/air-temperature', params=parameters, proxies=urllib.request.getproxies())

print(response.status_code)
# 200 is OK
# 403 Forbidden. No permission
# 404 No repponse

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


response_json = response.json()

print('response_json', response_json)

print ('JSON  json.dumps  response.json()')
jprint (response_json)


#  All the first level tags

api_info = response_json['api_info']
print ('API_INFO            ', api_info)

# notice the STATIONS is an array
stations = response_json['metadata']['stations']
print ('Length of Stations array ', len(stations))
reading_type = response_json['metadata']['reading_type']
reading_unit = response_json['metadata']['reading_unit']
print ('Reading Type            ', reading_type)
print ('Reading Unit            ', reading_unit)


items = response_json['items']
print ('Length of ITEMS array ', len(items))
print ('ITEMS            ', items)


