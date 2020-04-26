from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    """index页面视图"""
    return HttpResponse('ok')


def login(request):
    """重定向到index页面"""
    print("收到")
    return redirect("/index")
