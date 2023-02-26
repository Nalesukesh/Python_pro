import json

import requests

payload ={
    "name": "morpheus",
    "job": "leader"
}

print(type(payload))


post_resp=requests.post("https://reqres.in/api/users",data=payload)
print(post_resp)

json_resp=post_resp.json()

assert json_resp["job"]=="automatin" ,"Job post is doen-t match"

mydata=open("data.json","r").read()

resp=requests.post("",data=json.loads(mydata))



