from django.shortcuts import render, HttpResponse
from app.Token.login import Login
from app.Robot.Robot import Send
import requests
import json
import datetime
from app.models import content, Modular
from apscheduler.scheduler import Scheduler

sched = Scheduler()


class Login_modular:
    def __init__(self):
        Login().userLogin()
        super().__init__()

    def l_modular(self):
        with open('user.json', 'r') as f:
            url = json.load(f)['url']
        # con = content.objects.filter(modular_id=1)
        # modular = Modular.objects.filter(modular_name='登录模块')
        modular = Modular.objects.all()
        headers = Login().Read_Headers()
        for m in modular:
            con = content.objects.filter(modular_id=m.id)
            num = len(con)
            success = 0
            start_time = datetime.datetime.now()
            for i in con:
                # print(i.headers)
                if i.type == 'post':
                    cont = requests.post(url=url + i.headers, headers=headers, data=i.payload.encode('utf-8'),
                                         verify=False)
                    # print(type(i.payload))
                    try:
                        if 'code' in cont.json().keys() and cont.json()['code'] == 0:
                            success += 1
                            # print(i.headers)
                        else:
                            print('接口访问失败--->' + i.headers)
                            print(cont.json())
                    except Exception:
                        print('接口访问失败--->' + i.headers)
                    # if code in str(cont.json()):
                    #     success += 1
                else:
                    cont = requests.get(url=url + i.headers, params=i.payload.encode('utf-8'), headers=headers)
                    # print(i.payload)
                    try:
                        if 'code' in cont.json().keys() and cont.json()['code'] == 0:
                            success += 1
                            # print(i.headers)
                        else:
                            print('接口访问失败--->' + i.headers)
                            print(cont.json())
                    except Exception:
                        print('接口访问失败--->' + i.headers)
                    # if code in str(cont.json()):
                    #     print(1)
                    # if cont.status_code == 200:
                    #     success += 1
                # print(cont.json())
            msg = '执行' + str(num) + '个接口\n成功' + str(success) + '个\n'
            print(msg)
            Send().Send_msg(url, m.modular_name, start_time, num, success)
        # print(modular[0].modular_name)
        return HttpResponse('yes')


@sched.cron_schedule(hour=9, minute=10)
def mystack():
    Login_modular().l_modular()


sched.start()
