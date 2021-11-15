import requests
import json


uids={"魏铮":165143389,
      "贺静晗":108388169}


def get_right_code():
    right_code=[]
    flag = 0
    for i in range(1000,9999):
        url = 'https://wapi.weile.com/broadcast/wel-game/v2/receive/122/818/1.3.37.153.325/520500?format=json&code='+str(i)+'&userid=165143389'
        r = requests.post(url)
        if(json.loads(r.text)["msg"]!="领取失败，请出入正确的兑换码"):
            flag=flag+1
            right_code.append(i)
        if(flag==2):
          break
     return(right_code)

def get_bean_from_code(uid,right_code):
    for code in right_code:
        url = 'https://wapi.weile.com/broadcast/wel-game/v2/receive/122/818/1.3.37.153.325/520500?format=json&code='+str(code)+'&userid='+str(uid)
        r = requests.post(url)


def get_bean_from_luckyturn(uid):
    for i in range(20):
        url = 'https://wapi.weile.com/shake/turntable/draw/122/818/1.3.38.153.326/520101?format=json&userid='+str(uid)
        r = requests.post(url)
        url = "https://wapi.weile.com/shake/turntable/receive/122/818/1.3.38.153.326/520101?format=json&is_double=1&userid="+str(uid)
        r = requests.post(url)
        if(json.loads(r.text)['msg'] == '已经达到抽奖次数'):
            break

right_code = get_right_code()

for uid  in uids:
    try:
        get_bean_from_code(uids[uid],right_code)
        get_bean_from_luckyturn(uids[uid])
        print(uid,"搞定")
    except:
        print(uid,"没刷出来")

