from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime
from contact.get_contact import models

def hello(request):
	return HttpResponse("Hello world")

def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render_to_response('current_datetime_ahead.html',{'offset':offset,'dt':dt})

def login(request):
	return render_to_response('login.html')

def information(request):
	if 'studentnum' in request.GET and request.GET['studentnum']:
		studentnum = request.GET['studentnum']
		information = models.Information.objects.filter(studentnum=studentnum)
		return render_to_response("information.html",{'information':information})
	else:
		return render_to_response('login.html',{'error':True})