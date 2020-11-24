import requests
import urllib3
from django.http import HttpResponse


class CBA:
    def __init__(self):
        super().__init__()

    def get_msg(self):
        urllib3.disable_warnings()
        context = requests.get('https://matchweb.sports.qq.com/match/matchRound?competitionId=100008&roundNumbers=1&seasonId=2020&seasonType=regularSeason&from=H5&callback=reqwest_1605677479261',verify=False)
        print(type(context.text))
        print(context.text)
        return HttpResponse('yes')
