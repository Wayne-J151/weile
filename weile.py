import requests
import json
url = 'https://wapi.weile.com/broadcast/wel-game/v2/receive/122/818/1.3.37.153.325/520500?format=json&code=1233&userid=165143389'
r = requests.post(url)
print(r.text)
