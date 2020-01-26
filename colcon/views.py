from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import smtplib
#utilities

import pusher
pusher_client = pusher.Pusher(
  app_id='933316',
  key='f259e37a3a90ae0ee98e',
  secret='74b90e129d3ab0cafec1',
  cluster='ap2',
  ssl=True
)

def get_token(user):
    from uuid import uuid4
    import json
    from datetime import datetime
    auth,js = uuid4(),{}
    #pusher_client.trigger('my-channel', 'my-event', {'message': 'hello rishab'})
    with open('F:\Colconn\colcon\AUTH.json') as f:
        js =  json.load(f)
    js.update({int(auth):[user.username,str(datetime.now())]})
    with open('F:\Colconn\colcon\AUTH.json','w') as f:
        json.dump(js,f)
    return auth


#Views
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

@csrf_exempt
def forgot_password(req,id):
    try:
        if req.method != 'GET':
            return  HttpResponse(status = 405)
        if not id :
            return HttpResponse(status= 400)
        User.objects.get(username=id)
        #send_mail(id,'trial')
        return HttpResponse(status=200)
    except ObjectDoesNotExist :
        return HttpResponse(status=204)
    except Exception:
        return HttpResponse(str(Exception),status=500)


@csrf_exempt
def reset_password(req,id,pwd):
    try:
        if req.method != 'GET':
            return  HttpResponse(status = 405)
        if not (id and pwd):
            return HttpResponse(status= 400)
        user=User.objects.get(username=id)
        user.set_password(pwd)
        user.save()
        return HttpResponse(status=200)
    except ObjectDoesNotExist :
        return HttpResponse(status=204)
    except Exception:
        return HttpResponse(status=500)