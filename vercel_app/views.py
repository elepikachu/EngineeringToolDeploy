# -------------------------------------------------------------
# EngineeringTool/views.py
# 总视图函数
# -------------------------------------------------------------
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

VERSION = 'Engineering Toolbox 1.0.0'


# -------------------------------------------------------------
# 函数名： main_view
# 功能： 网站首页
# -------------------------------------------------------------
def main_view(request):
    dic = {'ver': VERSION}
    return render(request, 'main.html', dic)


# -------------------------------------------------------------
# 函数名： cxk_view
# 功能： 坤坤篮球
# -------------------------------------------------------------
def cxk_view(request):
    dic = {'ver': VERSION}
    return render(request, 'kun.html', dic)


# -------------------------------------------------------------
# 函数名： choose_view
# 功能： 随机选择器
# -------------------------------------------------------------
def choose_view(request):
    dic = {'ver': VERSION}
    return render(request, 'choose.html', dic)


# -------------------------------------------------------------
# 函数名： robots_txt
# 功能： robots.txt
# -------------------------------------------------------------
@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: *",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")