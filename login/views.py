#encoding: utf-8
__author__ = 'xwchen2'

from django.shortcuts import render_to_response
import datetime

def login(request):
    msg = 'login page'
    return render_to_response('msg.html', locals())

def logout(request):
    msg = 'logout page'
    return render_to_response('msg.html', locals())
