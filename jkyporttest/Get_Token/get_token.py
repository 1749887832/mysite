import requests
import urllib3


class Login_Test:

    def test_login(self):
        urllib3.disable_warnings()
        context = requests.post('http://172.10.62.94:3000/service-user/auth/employee',
                                json={"type": "employee", "identityType": 1, "ip": "0.0.0.0", "account": "13555555555", "password": "88888888", "assistant": False}, verify=False)
        token = context.json()['data']['token']
        print('==================>', token)
        return token
