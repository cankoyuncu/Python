import json

person_str = '{"name" : "Mario", "languages": ["python", "C"]}'
person_dict = '{"name" : Speed", "languages": "Spanish"}'

# JSON string to dict

result = json.loads(person_str)

# result= result["name"]
# result= result["languages"]

# with open("person.json") as f:
#     data = json.load(f)
#     # print(data)
#     print(data["name"])


# result = json.dumps(person_str)
# print(result)
# print(type(result))


#write to json file
# with open("person.json", "w") as f:
#     json.dump(person_str, f)

person_dict = json.loads(person_str)

result = json.dumps(person_dict, indent=4, sort_keys = True)

print(person_dict)
print(result)