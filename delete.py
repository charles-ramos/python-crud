import json
import http.client
connection = http.client.HTTPSConnection('parseapi.back4app.com', 443)
connection.connect()
connection.request('DELETE', '/classes/<CLASS-NAME>/<OBJECT-ID>', json.dumps({
       "score": 133,
       "playerName": "test Plott",
       "cheatMode": True
     }), {
       "X-Parse-Application-Id": "<APP-ID-HERE>",
       "X-Parse-REST-API-Key": "<REST-KEY-HERE>",
       "Content-Type": "application/json"
     })
result = json.loads(connection.getresponse().read().decode())
print (result)
