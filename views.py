from django.http import HttpResponse


def index(request):
    """index页面视图"""
    return HttpResponse('ok')