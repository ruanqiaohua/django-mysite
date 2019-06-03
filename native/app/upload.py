from django.http import HttpRequest, JsonResponse

def avatar(request: HttpRequest):
    data = {}
    msg = ""
    code = -1
    if not 'user' in request.POST:
        msg = "用户名不能为空"
        return JsonResponse({'code':code,'msg':msg,'data':data})
    return JsonResponse({'code':code,'msg':msg,'data':data})