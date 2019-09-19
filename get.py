import json
import http.client
connection = http.client.HTTPSConnection('parseapi.back4app.com', 443)
connection.connect()
connection.request('GET', '/classes/Likes/WrA5D0hZJu', '', {
       "X-Parse-Application-Id": "lOnJ1j6c5OHzz7RFmlXATbEqGvKA3BuT9KXGyWdO",
       "X-Parse-REST-API-Key": "sKio73fB6o0cAH7m0CbMaaHZk9GiAjiAQ5nzXYKL"
     })
result = json.loads(connection.getresponse().read().decode())
print (result)