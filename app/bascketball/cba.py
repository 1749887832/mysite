import requests
import urllib3
from django.http import HttpResponse
import json


class CBA:
    def __init__(self):
        super().__init__()

    def get_msg(self):
        urllib3.disable_warnings()
        context = requests.get(
            'https://matchweb.sports.qq.com/kbs/list?from=NBA_PC&columnId=100000&startTime=2020-12-18&endTime=2020-12-24',
            verify=False)
        # print(type(context.text))
        # print(context.text)
        data = json.loads(context.text)['data']
        for key, value in data.items():
            print(key)
            print(value)
            print(len(value))
            print(value[0]['mid'])
            print(value[0]['startTime'])
            print(value[0]['matchDesc'])
            print(value[0]['quarter'])
            print(value[0]['quarterTime'])
            print(value[0]['leftName'], value[0]['rightName'])
        return HttpResponse('yes')
