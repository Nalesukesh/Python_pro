import requests

resp=requests.get("https://reqres.in/api/users?page=2")
json_resp=resp.json()

print(json_resp['total_pages'])
assert json_resp['total_pages']==2, "total count doesn't matched"

print(json_resp['total'])
assert json_resp['total']==12, "total records does'n matched"

print(json_resp['data'][0]['email'])
assert json_resp["data"][0]["email"].endswith("reqres.in"), "email format is not matching"

print(json_resp["data"][0]["first_name"])
assert json_resp["data"][0]["first_name"]=="Michael", "first name does'n match"
