# coding: utf-8
from django.db import models

class Information(models.Model):
	studentnum = models.CharField(max_length=14,primary_key=True)
	password = models.CharField(max_length=20)
	name = models.CharField(max_length=10)
	phone = models.CharField(max_length=20)
	qq = models.CharField(max_length=15)
	email = models.CharField(max_length=50)
	job = models.CharField(max_length=50)
	company = models.CharField(max_length=200)
	postnum = models.PositiveIntegerField()
	addr = models.CharField(max_length=200)
	relation = models.PositiveIntegerField()
	weibo = models.CharField(max_length=50,null=True,blank=True)
	renren = models.CharField(max_length=50,null=True,blank=True)
	personal_home_page = models.CharField(max_length=200,null=True,blank=True)

	def __unicode__(self):
		return u'%s %s' % (self.studentnum, self.name)

	class Meta:
		db_table = 'information_2011'
		ordering = ['studentnum']

