import requests
import urllib3
from django.http import HttpResponse
import json
from apscheduler.schedulers.background import BackgroundScheduler
from app.Robot.NBA_Robot import N_Robot
import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import time

# 请求证书
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
sched = BackgroundScheduler()

count = 0


class NBA:
    def __init__(self):
        self.url = 'https://matchweb.sports.qq.com/kbs/matchStat?from=nba_database&selectParams=teamRank,periodGoals,playerStats,nbaPlayerMatchTotal,maxPlayers&mid='
        super().__init__()

    def get_msg(self):
        urllib3.disable_warnings()
        nowtime = datetime.datetime.now().strftime('%Y-%m-%d')
        print(nowtime)
        context = requests.get(
            'https://matchweb.sports.qq.com/kbs/list?from=NBA_PC&columnId=100000&startTime=' + nowtime + '&endTime=' + nowtime,
            verify=False)
        # print(type(context.text))
        # print(context.text)
        data = json.loads(context.text)['data']
        print(type(data))
        print(len(data))
        schedule = list()
        if len(data) == 0:
            schedule.append('今日没有比赛')
        else:
            for key, value in data.items():
                for j in value:
                    if j['leftName'] == '湖人' or j['rightName'] == '湖人':
                        sched.add_job(NBA().get_schedule, 'date', run_date=j['startTime'], args=[j], kwargs={},
                                      id='my_season')
                    msg = j['startTime'].split(' ')[-1] + '-->' + j['leftName'] + 'VS' + j['rightName']
                    schedule.append(msg)
            print(schedule)
        NBA().Return_msg(msg='今日比赛内容', date=schedule)
        return HttpResponse('yes')

    def get_schedule(self, *args):
        date = list()
        for i in args:
            msg = i['leftName'] + 'VS' + i['rightName'] + '---比赛开始'
            date.append(msg)
            NBA().Return_msg(msg='系统提示：', date=date)
            global mid
            mid = i['mid']
            sched.add_job(NBA().get_lakes, 'interval', minutes=1, args=[], id='my_job')
        return HttpResponse('yes')

    def get_lakes(self):
        global mid
        global count
        url = self.url + mid
        content = requests.get(url, verify=False, allow_redirects=False)
        data = json.loads(content.text)['data']['teamInfo']
        print(data)
        nowTime = data['quarterDesc']
        # 这是第几节
        # 第几节的时间
        if nowTime == '第1节 00:00' and count == 0:
            count = count + 1
            NBA().get_context(msg='第一节比赛结束', mid=mid)
            print('第一节比赛结束')
        elif nowTime == '第2节 00:00' and count == 1:
            count = count + 1
            NBA().get_context(msg='半场比赛结束', mid=mid)
            print('半场比赛结束')
        elif nowTime == '第3节 00:00' and count == 2:
            count = count + 1
            NBA().get_context(msg='第三节比赛结束', mid=mid)
            print('第三节比赛结束')
        elif nowTime == '第4节 00:00' and count == 3:
            count = 0
            NBA().get_context(msg='全场比赛结束', mid=mid)
            sched.remove_job('my_job')
            print('全场比赛结束')
        else:
            print(data['leftGoal'], data['rightGoal'])

        print(sched.get_jobs())
        return HttpResponse('yes')

    def get_context(self, msg=None, mid=None):
        url = self.url + mid
        content = requests.get(url, verify=False, allow_redirects=False)
        data = json.loads(content.text)['data']
        print(data['teamInfo']['leftFullCnName'])
        print(data['teamInfo']['rightFullCnName'])
        # print(data['playerStats']['left'])
        left_player = list()
        right_player = list()
        for i in data['playerStats']['left'][1:10]:
            left_date = i['row'][0] + '-->' + i['row'][3] + '分' + i['row'][4] + '篮板' + i['row'][5] + '助攻'
            left_player.append(left_date)
        for i in data['playerStats']['right'][1:10]:
            right_date = i['row'][0] + '-->' + i['row'][3] + '分' + i['row'][4] + '篮板' + i['row'][5] + '助攻'
            right_player.append(right_date)
        print(left_player)
        print(right_player)
        left_sum = data['periodGoals']['rows'][0][-1]
        right_sum = data['periodGoals']['rows'][1][-1]
        # for i in data['periodGoals']['rows'][0]:
        #     print(i)
        #     if i == '-':
        #         pass
        #     else:
        #         left_sum = int(i) + left_sum
        # for i in data['periodGoals']['rows'][1]:
        #     if i == '-':
        #         pass
        #     else:
        #         right_sum = int(i) + right_sum
        print(left_sum, right_sum)
        date = list()
        date.append(data['teamInfo']['leftFullCnName'] + '(' + str(left_sum) + ')——' + data['teamInfo'][
            'rightFullCnName'] + '(' + str(right_sum) + ')')
        NBA().Return_msg(msg=msg, date=date)
        NBA().Return_msg(msg=data['teamInfo']['leftFullCnName'] + '球员数据', date=left_player)
        NBA().Return_msg(msg=data['teamInfo']['rightFullCnName'] + '球员数据', date=right_player)
        return HttpResponse('yes')

    def Return_msg(self, msg=None, date=None):
        message = {"msg": msg, 'data': date}
        N_Robot().Send_msg(message=message)


@sched.scheduled_job('cron', hour=10, minute=5, id='my_main')
def mystack():
    NBA().get_msg()


sched.start()
