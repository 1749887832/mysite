import pytest
import requests
import urllib3
from django.http import HttpResponse

from app.models import Step, Case_models
from jkyporttest.common.Change_data import Change_data
from jkyporttest.common.Return_data import Return_msg
from jkyporttest.Get_Token.get_token import Login_Test

"""
    request_url:接口地址
    request_data:请求参数
    assert_variable:断言参数
    expect:断言期望
    assert_type:断言类型
    is_globals:是否获取参数
    response_variable:参数的字段（必须是后端返回的字段）
    use_variable:使用变量（不可重复）
    request_type:请求类型
    order_by:按照自定义顺序运行
"""


class Test_Msg(object):
    def __init__(self):
        self.data = None

    pass


class Test_Order:
    data = list()

    def setup_class(self):
        self.count = dict()
        print('每次都要执行这里')
        self.header = {'Content-Type': 'application/json;charset=UTF-8',
                       'Authorization': "Bearer " + Login_Test().test_login()}

    def teardown_class(self):
        Test_Order.data = []

    @pytest.mark.parametrize(
        ['case_id', 'request_url', 'request_data', 'assert_variable', 'expect', 'is_globals', 'response_variable', 'use_variable', 'request_type'], Test_Msg().data)
    def test_case(self, case_id, request_url, request_data, assert_variable, expect, is_globals, response_variable, use_variable, request_type):
        urllib3.disable_warnings()
        message = ''
        # 判断是否需要返回变量使用
        # print(self.count)
        if is_globals == 'false':
            # 判断是get还是post请求
            if request_type == 'post':
                context = requests.post(request_url, json=eval(Change_data().Changes_data(chang_data=request_data, data_dict=self.count)),
                                        headers=self.header, verify=False)
                print(request_url,'-----------')
                print(context.json())
            else:
                if request_data == '':
                    context = requests.get(Change_data().Changes_data(chang_data=request_url, data_dict=self.count), headers=self.header,
                                           verify=False)
                else:
                    context = requests.get(Change_data().Changes_data(chang_data=request_url, data_dict=self.count),
                                           params=eval(Change_data().Changes_data(chang_data=request_data, data_dict=self.count)),
                                           headers=self.header, verify=False)
            # 使用断言变量断言
            try:
                assert str(context.json()[assert_variable]) == str(expect)
            except Exception as e:
                print(e)
                if e == '':
                    message = ''
                else:
                    message = 'error'
            finally:
                if message == '':
                    Step.objects.filter(id=case_id).update(
                        result='成功'
                    )
                else:
                    Step.objects.filter(id=case_id).update(
                        result='失败'
                    )
        elif is_globals == 'true':
            if request_type == 'get':
                print(request_data)
                if request_data == ' ':
                    context = requests.get(Change_data().Changes_data(chang_data=request_url, data_dict=self.count), headers=self.header,
                                           verify=False)
                else:
                    context = requests.get(Change_data().Changes_data(chang_data=request_url, data_dict=self.count),
                                           params=eval(Change_data().Changes_data(chang_data=request_data, data_dict=self.count)),
                                           headers=self.header, verify=False)
            # 将断言变量放在字典中存储起来使用
            else:
                context = requests.post(request_url, json=eval(Change_data().Changes_data(chang_data=request_data, data_dict=self.count)),
                                        headers=self.header, verify=False)
            self.count[use_variable] = Return_msg().return_msg(context.json(), response_variable)
            try:
                assert str(context.json()[assert_variable]) == str(expect)
            except Exception as e:
                if e == '':
                    message = ''
                else:
                    message = 'error'
            finally:
                if message == '':
                    Step.objects.filter(id=case_id).update(
                        result='成功'
                    )
                else:
                    Step.objects.filter(id=case_id).update(
                        result='失败'
                    )

    def start_order_test(self):
        # print(Test_Order().data)
        case = Case_models.objects.filter(single_id=1)
        for c in case:
            step = Step.objects.filter(case_id=c.id).order_by('order_where')
            for i in step:
                context = [i.id, i.request_url, i.request_data, i.assert_variable, i.expect, i.is_globals, i.response_variable, i.use_variable,
                           i.request_type]
                Test_Order().data.append(context)
        pytest.main(['jkyporttest/Logic/Test_ordercase.py', '-s'])
        return HttpResponse('yes')
