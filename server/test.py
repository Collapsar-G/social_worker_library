import json

f = open('./static/config.json', 'r')
content = f.read()
config = json.loads(content)
f.close()
config['resources_list']["GroupData1"] =  ["./static/DATA/GroupData", "QQNum,QunNum"]
b = json.dumps(config)
f2 = open('./static/config.json', 'w')
f2.write(b)
f2.close()
