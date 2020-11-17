import requests
import json
url = 'http://127.0.0.1:8080'
#GET
print('GET')
print('[time in server] ' + requests.get(url).text)
print('[time in the requested area ] ' + requests.get(url+'/Asia/Tokyo').text)
print('[error: UnknownTimeZone] ' + requests.get(url+'/Asia/Tamsk').text)

#POST
print('POST')
data = {'tz_start': 'Asia/Tokyo', 'type': 'time'}
print('[time] ' + requests.post(url=url, data=json.dumps(data)).text)
data = {'type': 'time'}
print('[time, no location] ' + requests.post(url=url, data=json.dumps(data)).text)
data = {'tz_start': 'Asia/Tokyo'}
print('[time, no date] ' + requests.post(url=url, data=json.dumps(data)).text)
data = {'tz_start': 'Asia/Tokyo', 'type': 'date'}
print('[date] ' + requests.post(url=url, data=json.dumps(data)).text)
data = {'type': 'date'}
print('[date, no location] ' + requests.post(url=url, data=json.dumps(data)).text)
data = {'tz_start': 'Asia/Tokyo'}
print('[date, no type] ' + requests.post(url=url, data=json.dumps(data)).text)
data = {'tz_start': 'Europe/Moscow', 'type': 'datediff', 'tz_end': 'Asia/Tomsk'}
print('[beetwen, < ]' + requests.post(url=url, data=json.dumps(data)).text)
data = {'tz_start': 'Asia/Tomsk', 'type': 'datediff', 'tz_end': 'Europe/Moscow'}
print('[beetwen, >]' + requests.post(url=url, data=json.dumps(data)).text)
data = {'tz_start': 'Asia/Tomsk', 'type': 'datediff', 'tz_end': 'Asia/Tomsk'}
print('[beetwen, = ]' + requests.post(url=url, data=json.dumps(data)).text)
data = {'type': 'datediff'}
print('[beetwen, =, no location]' + requests.post(url=url, data=json.dumps(data)).text)
data = {'type': 'datediff', 'tz_end': 'Asia/Tokyo'}
print('[beetwen, =, no tz_start ]' + requests.post(url=url, data=json.dumps(data)).text)