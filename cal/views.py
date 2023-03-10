# -------------------------------------------------------------
# cal/views.py
# 计算器功能视图函数
# -------------------------------------------------------------
from django.shortcuts import render
from .calculation import CalculationFunc

VERSION = 'Engineering Toolbox 1.0.0'
DIC_PRS = {'Pa': 1, 'kPa': 1000, 'MPa': 1000000, 'atm': 101325}
DIC_TMP = {'K': 0, 'C': 273.15}


# -------------------------------------------------------------
# 函数名： steam_view
# 功能： 蒸汽计算器
# -------------------------------------------------------------
def steam_view(request):
    if request.method == 'GET':
        dic = {'ver': VERSION, 'res': False}
        return render(request, 'cal/steam.html', dic)
    elif request.method == 'POST':
        if 'cal' in request.POST:
            prs = request.POST['prs']
            prs2 = float(prs) * float(DIC_PRS[request.POST['uprs']])
            tmp = request.POST['tmp']
            tmp2 = float(tmp) + float(DIC_TMP[request.POST['utmp']])
            stm = request.POST['stm']
            res = CalculationFunc().water_steam_cal(prs2, tmp2, stm)
            dic = {'ver': VERSION, 'res': True}
            dic.update(res)
            print(dic)
            return render(request, 'cal/steam.html', dic)


# -------------------------------------------------------------
# 函数名： carbon_view
# 功能： 碳缺省值计算器
# -------------------------------------------------------------
def carbon_view(request):
    if request.method == 'GET':
        dic = {'ver': VERSION, 'res': False}
        return render(request, 'cal/carb.html', dic)
    elif request.method == 'POST':
        if 'cal' in request.POST:
            NCVi_q = request.POST['prs']
            EFi_q = request.POST['tmp']
            res = CalculationFunc().carbon_content_cal(NCVi_q, EFi_q)
            dic = {'ver': VERSION, 'res': True, 'z': res}
            return render(request, 'cal/carb.html', dic)


# -------------------------------------------------------------
# 函数名： calculator_view
# 功能： 迷你计算器
# -------------------------------------------------------------
def calculator_view(request):
    dic = {'ver': VERSION}
    return render(request, 'cal/cal.html', dic)
