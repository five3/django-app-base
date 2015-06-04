#encoding: utf-8
__author__ = 'xwchen2'

from django.shortcuts import render_to_response
import datetime
from login.models import User

def home(request):
    now = datetime.datetime.now()
    users = User.objects.all()
    print users
    return render_to_response('base.html', locals())

