import json
import requests
from requests_oauthlib import OAuth1

auth = OAuth1('0PlKlKMbNYWL9UeVuC6DPxX4B',
              'dpvpCGjA9udpjsPkCVfdxZhmAOLMXFeZcZEVLbH3usRiv8fHfN',
              '963011359737774080-mYiiiIGOarKbuYGVdVTJBPcYC39RkqC',
              'f8031GVQo6dJXX35RRVbDlGxMcitrAt7uyAUVgKuO1E0R')

r = requests.get("https://api.twitter.com/1.1/friends/list.json?", auth=auth)
info = json.loads(r.text)
print(info)
json.dump(info, open("info.json", "w", encoding="utf-8"), ensure_ascii=False)
