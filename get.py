import json
import http.client
connection = http.client.HTTPSConnection('parseapi.back4app.com', 443)
connection.connect()
connection.request('GET', '/classes/<CLASS-NAME>/<OBJECT-ID>', '', {
       "X-Parse-Application-Id": "<APP-ID-HERE>",
       "X-Parse-REST-API-Key": "<REST-KEY-HERE>"
     })
result = json.loads(connection.getresponse().read().decode())
print (result)
