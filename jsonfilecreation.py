import json

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 3,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("metadata.json", "w") as outfile:
    outfile.write(json_object)