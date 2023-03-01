import json

info ='{"name":"aman","age":20,"email":"amankhadse@gmail.com"}'
parsed = json.loads(info)
print(parsed)


#Formatting JSON output
print(json.dumps(info))


print(json.dumps(info,indent=3))

#Creating JSON from Python dict
import json
d = {
'mango': 'yellow',
'aman': 1,
'numbers': [1, 2, 3]
} 
 
print(json.dumps(d))

#Creating Python dict from JSON
import json
s = '{"numbers": [1, 2, 3], "mango": "yellow", "aman": 1}'
print(json.loads(s))