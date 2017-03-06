import json
import datetime


ids = "ec2-slslskerfw352r-asu9u-wut="

item = json.dumps(json.loads(json.dumps("sting": {"date":datetime.datetime.now().isoformat(),"ec2instanceid":ids})))

print(item)
print(type(item))
