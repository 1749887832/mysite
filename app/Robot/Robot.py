import requests
import time
import hmac
import hashlib
import base64
import urllib.parse

import urllib3
import datetime


class Send:
    def __init__(self):
        super().__init__()
        self.secret = 'SEC041656cff29539d7185b4b566d1ac00e70b4cdcff2ee384f7bc71c86a9301184'
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token=55544863b0b1488ea5364cc5c25bb8a86868c609ccf707e3b050259b97ba8d4f'

    def get_secret(self):
        secret_enc = self.secret.encode('utf-8')
        timestamp = str(round(time.time() * 1000))
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return self.url + '&timestamp={0}&sign={1}'.format(timestamp, sign)

    def Send_msg(self, url, modular, start_time, num, success):
        su = round(success / num * 100, 2)
        # print(round(1/3*100,2))
        # print(type(su))
        if su < 100.0:
            result = "失败"
        else:
            result = '成功'
        error_su = round(100 - su, 2)
        error = int(num) - int(success)
        end_time = datetime.datetime.now()
        # print(end_time-start_time)
        message = f"接口测试概要：{url}\n测试系统：极运营\n测试模块：{modular} \n整体结果：{result} \n测试开始时间：{str(start_time)}" \
                  f"\n测试结束时间：{str(end_time)}\n持续时间：{str((end_time - start_time).seconds)}s\n接口测试总数：{str(num)}\n" \
                  f"成功：{str(success)}||失败：{str(error)} \n测试成功率：{str(su)}%\n测试失败率：{str(error_su)}%"
        print(message)
        url = self.get_secret()
        # print(url)
        headers = {
            'Content-Type': 'application/json'
        }
        json = {"msgtype": "text",
                "text": {
                    "content": message
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
        urllib3.disable_warnings()
        resp = requests.post(url=url, headers=headers, json=json, verify=False)
        print(resp.text)
