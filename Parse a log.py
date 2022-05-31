###Log Sample
###2022-10-26 10:26:44 | https://myweb.com/home | SUCCESS | Hello Everyone
###2022-10-26 10:26:54 | https://myweb.com/about | SUCCESS | we are going to parse a log
###2022-10-26 10:27:01 | https://myweb.com/page | ERROR | what do we want to know?
###2022-10-26 10:27:03 | https://myweb.com/user/me | SUCCESS | lets get it started
###2022-10-26 10:27:04 | https://myweb.com/settings/ | ERROR | Done!


import json

file_name = "test.txt"
file = open(file_name, "r")
data = []
order = ["date", "url", "type", "message"]

for line in file.readlines():
    details = line.split("|")
    details = [x.strip() for x in details]
    structure = {key: value for key, value in zip(order, details)}
    data.append(structure)

for entry in data:
    print(json.dumps(entry, indent=4))