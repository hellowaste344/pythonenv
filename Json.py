import json

# JSON string
emp = '{"id":"09", "name": "nitin", "department": "finance"}'
print("This is JSON", type(emp))

print("\nNow convert from JSON to Python")

# convert string to python dict
d = json.loads(emp)
print("converted to pyhton", type(d))
print(d)
'''
# convert python dict to JSON
d = {"id": "09", "name": "nitin", "department": "finance"}
obj = json.dumps(d, indent=4)
print("converted to JSON:\n", type(obj))
print(obj)

data_to_write = {"name": "X-Ashe", "age": 20, "skills": ["Python", "C++"]}

with open("sample.json", "w") as f:
    # json.dump(obj, file, ...)
    json.dump(data_to_write, f, indent=4)

# read from file and parse json
with open("sample.json", "r") as f:
    data = json.load(f)

print(type(data))
print(data)
'''