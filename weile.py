import requests
import json
j=0

for i in range(9999):
  i=i+1000
  url = 'https://wapi.weile.com/broadcast/wel-game/v2/receive/122/818/1.3.37.153.325/520500?format=json&code='+str(i)+'&userid=165143389'
  r = requests.post(url)
  if(json.loads(r.text)["msg"]!="领取失败，请出入正确的兑换码"):
    j=j+1
    print(i)
    print("成功")
    if(j>3):
      break
for i in range(9999):
  i=i+1000
  url = 'https://wapi.weile.com/broadcast/wel-game/v2/receive/122/818/1.3.37.153.325/520101?format=json&code='+str(i)+'&userid=108388169'
  r = requests.post(url)
  if(json.loads(r.text)["msg"]!="领取失败，请出入正确的兑换码"):
    j=j+1
    print(i)
    print("成功")
    if(j>3):
      break

