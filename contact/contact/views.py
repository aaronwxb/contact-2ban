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
	userinfo = models.Information.objects.get(studentnum = request.user.username)
	return render_to_response('modify_info.html', {'personalinfo': userinfo})

@login_required
def handle_modify(request):
	# TODO 这里根据提交上来的数据修改个人信息
	userinfo = models.Information.objects.get(studentnum = request.user.username)
	print request.POST.get('studentnum', '')
	if userinfo.studentnum != request.POST.get('studentnum', ''):
		# TODO 不能修改他人信息
		return HttpResponseRedirect('/error/')
	userinfo.phone = request.POST.get('phone', '')
	userinfo.qq = request.POST.get('qq', '')
	userinfo.email = request.POST.get('email', '')
	userinfo.job = request.POST.get('job', '')
	userinfo.company = request.POST.get('company', '')
	userinfo.postnum = request.POST.get('postnum', '')
	userinfo.addr = request.POST.get('addr', '')
	userinfo.relation = request.POST.get('relationship', '')
	userinfo.weibo = request.POST.get('weibo', '')
	userinfo.renren = request.POST.get('renren', '')
	userinfo.personal_home_page = request.POST.get('personal_home_page', '')
	userinfo.save()
	# 修改成功则重定向到个人信息修改页面
	return HttpResponseRedirect('/modifyinfo/')

def modifysuccess(request):
	return render_to_response('modify_success.html')

@login_required
def classall(request):
	information = models.Information.objects.filter()
	print information.count
	return render_to_response('classall.html', {'information': information})
