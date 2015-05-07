from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
from utils.decorators import render_to
from models import *
#from django.core.context_processors import csrf
#from django.http import HttpResponseRedirect
#from django.contrib.auth.models import User
#
#import datetime
#import json
#from dateutil import parser

#@login_required
@render_to('index.html')
def index(request):
    res = { 'test': 'test' }
    return res

@render_to('map.html')
def questmap(request):
    res = { 'test': 'test' }
    return res

@render_to('index.html')
def addtask(request):
	task = Task()

	task.MEMBER_CHOICES = request['MEMBER_CHOICES']

    task.user_create = request.user
    task.task_type = TaskType.objects.filter(id = request['task_type'])
    task.category = Category.objects.filter(id = request['category'])

    task.member_type = request['member_type']
    task.title = request['title']
    task.text_content = request['text_content']
    task.video_link = request['video_link']
    task.members_min = request['members_min']
    task.members_max = request['members_max']
    task.cost_need = request['cost_need']
    task.cost_now = request['cost_now']
    task.min_level = request['min_level']
    task.date_start = request['date_start']
    task.date_finish = request['date_finish']
    task.date_add = request['date_add']
    task.geojson = request['geojson']

	res = { 'test': 'test' }
    return res