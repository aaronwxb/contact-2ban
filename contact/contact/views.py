#coding:utf-8
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from contact.get_contact import models
from contact.forms import PersonalInfo


def login(request):
	return render_to_response('login.html')

def information(request):
	error = False;
	if 'studentnum' in request.GET:
		studentnum = request.GET['studentnum']
		if not studentnum:
			error = True
		else:
			information = models.Information.objects.filter(studentnum=studentnum)
			return render_to_response("information.html",{'information':information})
	return render_to_response('login.html',{'error':error})

def modifyinfo(request):
	if request.method == 'POST':
		form = PersonalInfo(request.POST)
		if form.is_valid():
			cd = form.cleaned_data

			return HttpResponseRedirect('/modifyinfo/success/')
	else:
		form = PersonalInfo(
			initial={'name':'太2了！'}
		)
	return render_to_response('modify_info.html',{'form':form})

def modifysuccess(request):
	return render_to_response('modify_success.html')
