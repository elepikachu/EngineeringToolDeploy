# -------------------------------------------------------------
# cal/url.py
# 计算器功能url声明
# -------------------------------------------------------------
from django.urls import path
from . import views


urlpatterns = [
    path('steam', views.steam_view),
    path('calculator', views.calculator_view),
    path('carbon', views.carbon_view),
    ]