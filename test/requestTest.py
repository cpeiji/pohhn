import requests


payload = {'mid': '15834498'}
header = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
          }
r = requests.get("http://www.dytt8.net/index.htm", params="",headers="")
r.encoding = 'gbk'
print(r.text)