from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
# Create your views here.
def get_token(user):
    from uuid import uuid4
    import json
    from datetime import datetime
    auth,js = uuid4(),{}
    with open('F:\Colconn\colcon\AUTH.json') as f:
        js =  json.load(f)
    js.update({int(auth):[user.username,str(datetime.now())]})
    with open('F:\Colconn\colcon\AUTH.json','w') as f:
        json.dump(js,f)
    return auth
@csrf_exempt
def login(req):
    try:
        if req.method != 'POST':
            return  HttpResponse(status = 405)
        id = req.POST.get("id")
        pwd = req.POST.get("pwd")
        if not (id and pwd):
            return HttpResponse(status= 400)
        user = authenticate(username=req.POST.get("id"), password=req.POST.get("pwd"))
        if user:
            auth = get_token(user)
            return JsonResponse({"msg":"login successful","auth":auth},status=200)
        else:
            return HttpResponse(status = 401)
    except Exception:
        return HttpResponse(status=500)

