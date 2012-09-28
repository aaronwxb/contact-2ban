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

def personalpage(request):
	
	"""error = False;
	if 'studentnum' in request.GET:
		studentnum = request.GET['studentnum']

		if not studentnum:
			error = True
			errinfo = "学号不能为空"
		else:
			if 'password' in request.GET:
				password = request.GET['password']
				if not password:
					error = True
					errinfo = "密码不能为空"
				else:
					personalinfo = models.Information.objects.filter(studentnum=studentnum,password=password)
					if personalinfo:
						return render_to_response("personalpage.html",{'personalinfo':personalinfo})
					else:
						err = True
						errinfo = "请输入正确的本科学号和密码，初始密码为123456"
						return render_to_response('login.html',{'error':error,'errinfo':errinfo})
	return render_to_response('login.html',{'error':error,'errinfo':errinfo})"""
	if request.method == 'POST':
		form = LoginInfo(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			personalinfo = models.Information.objects.filter(studentnum=cd.studentnum,password=cd.password)
			return render_to_response("personalpage.html",{'personalinfo':personalinfo})
	else:
		form = LoginInfo(
			initial={
				'studentnum':'本科学号',
				'password':'初始密码为123456',
			}
		)
	return render_to_response('login.html',{'form':form})


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
