import json

from django.http import HttpResponse

from models import Task

def send_all_geo_points(request):
	response_data = {}

	tasks = Task.objects.all()

	for task in tasks:
		response_data['title'] = task.title
		response_data['geo'] = task.geojson
	return HttpResponse(json.dumps(response_data), content_type="application/json")