from django.http import JsonResponse, HttpRequest
from .models import User

def login(request: HttpRequest):

    data = {}
    msg = ""
    code = -1

    if not 'user' in request.GET:
        msg = "用户名不能为空"
        return JsonResponse({'code':code,'msg':msg,'data':data})

    if not 'password' in request.GET:
        msg = "密码不能为空"
        return JsonResponse({'code':code,'msg':msg,'data':data})
    # 用户名和密码
    user = request.GET['user']
    password = request.GET['password']

    if len(user) < 6:
        msg = '用户名不能小余6位数'
        return JsonResponse({'code':code,'msg':msg,'data':data})
    
    if len(password) < 6:
        msg = '密码不能小余6位数'
        return JsonResponse({'code':code,'msg':msg,'data':data})
    # 已登录
    if 'user' in request.session:
        if user == request.session['user']:
            msg = '已登陆'
            return JsonResponse({'code':code,'msg':msg,'data':data})
    # login
    try:
        userDB = User.objects.get(name=user)
    except User.DoesNotExist:
        msg = "用户名不存在"
    else:
        if userDB.password == password:
            code = 0
            msg = "登录成功"
            request.session['user'] = userDB.name
        else:
            msg = "用户名或密码错误！"

    return JsonResponse({'code':code,'msg':msg,'data':data})


def register(request: HttpRequest):

    data = {}
    msg = ""
    code = -1

    if 'user' and 'password' in request.GET == False:
        msg = "用户名或密码不能为空"
        return JsonResponse({'code':code,'msg':msg,'data':data})
    # 用户名和密码
    user = request.GET['user']
    password = request.GET['password']

    if len(user) < 6:
        msg = "用户名不能小余6位数"
        return JsonResponse({'code':code,'msg':msg,'data':data})

    if len(password) < 6:
        msg = "密码不能小余6位数"
        return JsonResponse({'code':code,'msg':msg,'data':data})
    # register
    try:
        User.objects.get(name=user)
    except User.DoesNotExist:
        userDB = User()
        userDB.name = user
        userDB.password = password
        userDB.save()
        data = {
        'user':user,
        'password':password
        }
        code = 0
        msg = "注册成功"
    else:
        msg = "用户名已存在"
    return JsonResponse({'code':code,'msg':msg,'data':data})

def logout(request: HttpRequest):

    data = {}
    msg = "登出成功"
    code = 0

    try:
        del request.session['user']
    except KeyError:
        pass
    return JsonResponse({'code':code,'msg':msg,'data':data})
