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
	personalinfo = PersonalInfo(request.POST)
	if personalinfo.is_valid() == False:
		errinfo = personalinfo.errors
		return render_to_response('error.html', {'errinfo': errinfo})
	print personalinfo.cleaned_data
	userinfo = personalinfo.cleaned_data	
	if userinfo['studentnum'] != request.POST.get('studentnum', ''):
		errinfo = "不能修改他人信息"
		# TODO 不能修改他人信息
		return render_to_response('error.html', {'errinfo': errinfo})
	saveinfo = models.Information.objects.get(studentnum = request.user.username)
	saveinfo.phone = request.POST.get('phone', '')
	saveinfo.qq = request.POST.get('qq', '')
	saveinfo.email = request.POST.get('email', '')
	saveinfo.job = request.POST.get('job', '')
	saveinfo.company = request.POST.get('company', '')
	saveinfo.postnum = request.POST.get('postnum', '')
	saveinfo.addr = request.POST.get('addr', '')
	saveinfo.relation = request.POST.get('relation', '')
	saveinfo.weibo = request.POST.get('weibo', '')
	saveinfo.renren = request.POST.get('renren', '')
	saveinfo.personal_home_page = request.POST.get('personal_home_page', '')
	saveinfo.save()
	# 修改成功则重定向到个人信息修改页面
	return HttpResponseRedirect('/modifyinfo/success/')
@login_required
def modifysuccess(request):
	return render_to_response('modify_success.html')
@login_required
def error(request):
	errinfo = request.errinfo
	return render_to_response('error.html', {'errinfo': errinfo})
@login_required
def about(request):
	return render_to_response('about.html')

@login_required
def classall(request):
	information = models.Information.objects.filter()
	print information.count
	return render_to_response('classall.html', {'information': information})
