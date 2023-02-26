import requests

resp=requests.get("https://reqres.in/api/users?page=2")
print(resp)
print(type(resp))
print(dir(resp))
code=resp.status_code
print(code)

assert code==200 ,"Code doesn't match"
#print(resp.text)
#print(resp.content)
json_resp=resp.json()
print(resp.json())
# print(resp.headers)
# print(type(resp.headers))
# print(resp.cookies)
# print(resp.url)
# print(resp.encoding)

print(json_resp["support"]["url"])
assert json_resp["support"]["url"]=="https://reqres.in/#support-heading" ,"url doesn't match"




