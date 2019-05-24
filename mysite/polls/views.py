from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("hello world !")

def info(request):
    data = {
        'code':0,
        'message':'请求成功',
        'data':[1,2,3,4,5],
    }
    return JsonResponse(data)