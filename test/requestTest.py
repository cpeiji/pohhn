import requests


payload = {'mid': '15834498'}
r = requests.get("http://space.bilibili.com/ajax/member/getSubmitVideos", params=payload,headers="")
print(r.json())