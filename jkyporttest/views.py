from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def open(request):
    return render(request, 'indnx.html')


def create(request):
    print(request.POST)
    print(request.POST.get('request_url'))
    print(request.POST.get('request_data'))
    print(request.POST.get('assert_variable'))
    print(request.POST.get('expect'))
    print(request.POST.get('assert_type'))
    print(request.POST.get('is_globals'))
    print(request.POST.get('response_variable'))
    print(request.POST.get('use_variable'))
    print(request.POST.get('request_type'))
    return render(request, 'indnx.html')


def ceshi(request):
    print(request)
    data = [{'code': '0', 'msg': '成功'}]
    return JsonResponse(data=data, safe=False)
