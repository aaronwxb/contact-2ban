# coding: utf-8
from django.db import models

class Information(models.Model):
	studentnum = models.CharField(max_length=14,primary_key=True)
	name = models.CharField(max_length=10)
	phone = models.CharField(max_length=20)
	qq = models.CharField(max_length=15)
	email = models.EmailField()
	job = models.CharField(max_length=30)
	company = models.CharField(max_length=100)
	postnum = models.PositiveIntegerField()
	addr = models.CharField(max_length=100)
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
	relation = models.PositiveIntegerField(choices=RELATION_STATUS)
	weibo = models.CharField(max_length=50)
	renren = models.CharField(max_length=50)
	personal_home_page = models.URLField()

	#modify_time = models.DateField(auto_now)

	def __unicode__(self):
		return u'%s %s' % (self.studentnum, self.name)

	class Meta:
		db_table = 'information_2011'
		ordering = ['studentnum']


