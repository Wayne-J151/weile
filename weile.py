import requests
import json


uids=[165143389,108388169]

def get_bean_from_code(uid):
    flag = 0
    for i in range(1000,9999):
        url = 'https://wapi.weile.com/broadcast/wel-game/v2/receive/122/818/1.3.37.153.325/520500?format=json&code='+str(i)+'&userid='+str(uid)
        r = requests.post(url)
        if(json.loads(r.text)["msg"]!="领取失败，请出入正确的兑换码"):
            flag=flag+1
            print(i)
            print("成功")
        if(flag>1):
          break


def get_bean_from_luckyturn(uid):
    for i in range(20):
        url = 'https://wapi.weile.com/shake/turntable/draw/122/818/1.3.38.153.326/520101?format=json&userid='+str(uid)
        r = requests.post(url)
        url = "https://wapi.weile.com/shake/turntable/receive/122/818/1.3.38.153.326/520101?format=json&is_double=1&userid="+str(uid)
        r = requests.post(url)
        if(json.loads(r.text)['msg'] == '已经达到抽奖次数'):
            break

 
for uid  in uids:
    
    get_bean_from_code(uid)
    get_bean_from_luckyturn(uid)

