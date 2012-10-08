#coding:utf-8
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from contact.get_contact import models
from contact.forms import PersonalInfo
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def login(request):
	return render_to_response('login.html')

def check_login(request):
	"""verify the username and password
	
	"""
	username = request.POST.get('studentnum', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username = username, password = password)
	
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/personalpage/')
	else:
		return HttpResponseRedirect('/login/')
	
@login_required
def personalpage(request):
	userinfo = models.Information.objects.get(studentnum = request.user.username)
	return render_to_response('personalpage.html', {'personalinfo': userinfo})

@login_required
def modifyinfo(request):
	return render_to_response('modify_info.html')
			print cd['name']
			personalinfo = models.Information.objects.get(studentnum = request.user.username)
			personalinfo.name = cd['name']
			personalinfo.phone = cd['phone']
			personalinfo.save()
def modifysuccess(request):
	return render_to_response('modify_success.html')

@login_required
def classall(request):
	information = models.Information.objects.filter()
	print information.count
	return render_to_response('classall.html', {'information': information})
