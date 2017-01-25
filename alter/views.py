from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from qbot import Qbot
# Create your views here.

def hello(request):
    return HttpResponse('Hello.')

@csrf_exempt
def start(request):

    Qbot.start()

    return HttpResponse('Success.')

@csrf_exempt
def send(request):
    try:
        msg = request.POST['msg']
    except:
        msg = 'empty msg'

    Qbot.send(msg)

    return HttpResponse('Success.')
