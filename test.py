import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 78, "name": "Joe", "views": 100},
        {"likes": 10, "name": "How to make REST API", "views": 20000},
        {"likes": 10, "name": "Hi", "views": 100}]


for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i] )
    print(response.json())


#input()
#response = requests.delete(BASE + "video/0")
#print(response)

input()
response = requests.get(BASE + "video/6")
print(response.json())

response = requests.get(BASE + "video/0")
print(response.json())