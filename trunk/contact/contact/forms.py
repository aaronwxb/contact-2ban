#coding:utf-8
from django import forms
from django.contrib.localflavor.cn.forms import CNPostCodeField,CNCellNumberField

class PersonalInfo(forms.Form):
	studentnum = forms.CharField(max_length=14,label="学号")
	name = forms.CharField(max_length=10,label="姓名")
	phone = forms.CharField(max_length=11,label="手机")
	qq = forms.IntegerField(label="QQ")
	email = forms.EmailField(label="邮箱")
	job = forms.CharField(max_length=30,label="职称")
	company = forms.CharField(max_length=100,widget=forms.Textarea,label="单位")
	postnum = forms.CharField(max_length=6,min_length=6,label="邮编")
	addr = forms.CharField(max_length=100,widget=forms.Textarea,label="地址")
	RELATION_STATUS = (
		('0','单身'),
		('1','有男朋友'),
		('2','有女朋友'),
		('3','已婚'),
		('31','纸婚'),
		('310','锡婚'),
		('320','瓷婚'),
		('330','珍珠婚'),
		('340','红宝石婚'),
		('350','金婚'),
		('4','离婚'),
		('5','二婚'),
	)
	relation = forms.ChoiceField(choices=RELATION_STATUS,label="感情状态")
	weibo = forms.CharField(max_length=50,required=False,label="微博")
	renren = forms.CharField(max_length=50,required=False,label="人人")
	personal_home_page = forms.URLField(required=False,label="个人主页")
