import requests

BASE = "http://127.0.0.1:5000/"

# sampleResponse = requests.get(BASE + "sample/charaka/22")
# print(sampleResponse)

# Sample data to add
data = [{"name": "A", "views": 1200, "likes": 100}, 
        #{"name": "B"},
        {"name": "C", "views": 48, "likes": 13},
        {"name": "D", "views": 213451, "likes": 13012},
        {"views": 48, "likes": 8},
        {"name": "E", "views": 3500, "likes": 2100},
        {"name": "F", "views": 852}]
 
 # Send requests to add sample data
for i in range(len(data)):
    videoResponse = requests.post(BASE + "video/" + str(i), data[i])
    print(videoResponse.json())

input()

res = requests.get(BASE + "video/2")
print(res.json())

'''
videoResponse = requests.delete(BASE + "video/2")
print(videoResponse.json()) 

videoResponse = requests.delete(BASE + "video/5")
print(videoResponse.json()) 
'''
