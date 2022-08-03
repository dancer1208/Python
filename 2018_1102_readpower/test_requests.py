import requests
r=requests.get("http://120.119.72.60:5566")
r.status_code
r.encoding='utf-8'
r.text
print(r.text)
