from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from colcon.models import Profile
from django.core.exceptions import ObjectDoesNotExist
import math, random
from django.core.mail import send_mail
from django.conf import settings
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


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def forgot_email(receiver,msg = ''):
    subject = 'Otp to change password'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [receiver,]
    send_mail( subject, msg, email_from, recipient_list )
    #return redirect('redirect to a new page')

def activate_email(receiver,msg = ''):
    subject = 'Link to Activate Account'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [receiver,]
    send_mail( subject, msg, email_from, recipient_list )
    #return redirect('redirect to a new page')

def encrypt(msg):
    msg = str(msg)
    temp = ''
    for x in msg:
        temp += chr(ord(x)+13)
    return temp[::-1]
    #return msg


def decrypt(msg):
    msg = msg[::-1]
    temp = ''
    for x in msg:
        temp += chr(ord(x)-13)
    return temp




####################################################################################################################################################################################################################################################################################################################################



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
            temp = Profile.objects.get(user = user)
            if not temp.activated:
                token = encrypt(user.username)
                activate_email(str(temp.email),'http://127.0.0.1:8000/colcon/activate/'+token)
                return HttpResponse(status = 403)
            auth = get_token(user)
            return JsonResponse({"msg":"login successful","auth":auth},status=200)
        else:
            return HttpResponse(status = 401)
    except Exception:
        print(Exception.__str__())
        return HttpResponse(status=500)


@csrf_exempt
def activate(req,id):
    pass
@csrf_exempt
def forgot_password(req,id):
    try:
        if req.method != 'GET':
            return  HttpResponse(status = 405)
        if not id :
            return HttpResponse(status= 400)
        User.objects.get(username=id)
        otp = generateOTP()
        forgot_email(id,'OTP:'+otp)
        return JsonResponse({'otp':otp},status=200)
    except ObjectDoesNotExist :
        return HttpResponse(status=204)
    except Exception:
        return HttpResponse(status=500)


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