import requests
import json

from app.models import Server


class Login:
    def __init__(self):
        self.account = 13555555555
        self.password = 88888888
        self.msg = {"type": "employee", "identityType": 1, "ip": "0.0.0.0", "account": self.account,
                    "password": self.password, "assistant": False}
        self.userLogin()

    def userLogin(self):
        server = Server.objects.all()
        for i in server:
            # print(i.server)
            if i.server == 'http://192.168.32.42:3000':
                context = requests.post(i.server + '/service-user/auth/employee', json=self.msg, verify=False)
                # print(context.status_code)
                if context.status_code == 200 and context.json()['msg'] == '成功':
                    content = {
                        'user': self.account,
                        'password': self.password,
                        'token': context.json()['data']['token'],
                        'url': i.server,
                        'headers': {'Content-Type': 'application/json;charset=UTF-8',
                                    'Authorization': "Bearer " + context.json()['data']['token']}
                    }
                    with open('user.json', 'w') as f:
                        json.dump(content, f)
                    # print(context.json()['data']['token'])
                else:
                    # return '错误'
                    print('请求错误或用户名或密码错误')

    def Read_Headers(self):
        with open('user.json', 'r') as f:
            msg = json.load(f)
            return msg['headers']
