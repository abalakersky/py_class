import json

ids = "ec2-slslskerfw352r-asu9u-wut="

item = json.loads(json.dumps({"date":datetime.datetime.now().isoformat(),"ec2instanceid":ids}))

print(item)