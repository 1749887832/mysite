import requests
import time
import hmac
import hashlib
import base64
import urllib.parse

import urllib3
import datetime


class N_Robot:
    def __init__(self):
        super().__init__()
        self.secret = 'SEC2cce3ec36703fd03c7232bde4557fd64e4cc9e693cf8f2c615fa97a9682192fc'
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token=b5c0e88dbbff6d251c748fb7d1a3e376be51409d7de787c82dd918a22e0a75d3'

    def get_secret(self):
        secret_enc = self.secret.encode('utf-8')
        timestamp = str(round(time.time() * 1000))
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return self.url + '&timestamp={0}&sign={1}'.format(timestamp, sign)

    def Send_msg(self, message=None):
        # print(round(1/3*100,2))
        # print(type(su))
        # print(end_time-start_time)
        print(message)
        msg = message['msg']
        date = "### " + msg + '\n> '
        for i in message['data']:
            date = date + i + '\n\n> '
        # print(date)
        url = self.get_secret()
        # print(url)
        headers = {
            'Content-Type': 'application/json'
        }
        json = {"msgtype": "markdown",
                "markdown": {
                    "title": msg,
                    "text": date,
                },
                "at": {
                    # 这里是输入@人的电话号码
                    "atMobiles": [
                        # '18258224033',
                        # '17623669485'
                    ]
                },
                # 设置是否@所有人
                'isAtAll': False
                }
        # urllib3.disable_warnings()
        # resp = requests.post(url=url, headers=headers, json=json, verify=False)
        # print(resp.text)
