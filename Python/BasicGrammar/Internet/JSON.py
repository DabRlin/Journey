import json

json_string = '{"name":"John","age":"30"}';
json_object = json.loads(json_string)

print(json_object["name"])

json_object = {"name":"ALice","age":90}
json_string = json.dumps(json_object)
print(json_string)