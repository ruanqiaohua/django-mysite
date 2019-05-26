from django.urls import path
from . import views, login

urlpatterns = [
    path('', views.index, name='index'),
    path('info', views.info, name='info'),
    path('login', login.login, name='登录'),
    path('register', login.register, name='注册'),
    path('logout', login.logout, name='登出'),
]
