import requests
import random

from hashlib import md5


def baiduTranslate(from_lang,to_lang,query,appid,appkey):
    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)
    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    #print(json.dumps(result, indent=4, ensure_ascii=False))
    resultString = assemble(result)
    return resultString


def assemble(result):
    resultString = ""
    #print(result)
    for i in result['trans_result']:
        resultString += i['dst'] + "\n"

    return str(resultString)


def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

