
from django.urls import path
from . import views, login, upload

urlpatterns = [
    path('', views.index, name='index'),
    path('login', login.login, name='登录'),
    path('register', login.register, name='注册'),
    path('logout', login.logout, name='登出'),
    path('upload/avatar', upload.avatar, name='上传头像'),
]
