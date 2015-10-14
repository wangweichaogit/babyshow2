#coding=utf-8
from django.db import models
from datetime import datetime,timedelta
from django.contrib.auth.models import User
# Create your models here.

#选手信息表
class PlayerInfo(models.Model):
	pi_name = models.CharField(max_length =32,verbose_name = u'宝宝姓名')
	pi_phone = models.CharField(max_length = 32,unique = True,verbose_name = u'联系电话')
	pi_photo = models.ImageField(upload_to = "media/uploads/",verbose_name = u'宝宝照片')
	pi_desc = models.CharField(max_length = 100,verbose_name = u'描述信息')
	pi_time = models.DateTimeField(default = datetime.now,verbose_name = u'报名时间')
	pi_tickets = models.IntegerField(default = 0,verbose_name = u'当前票数')
	pi_ranking  = models.IntegerField(default = 0)

	def __unicode__(self):
		return str(self.id)

#class UserProfile(models.Model):
#	user = models.OneToOneField(User)
#	website = models.URLField(blank = True)
#	def __unicode__(self):
#		return self.user.username
#注册用户信息
class Userinfo(models.Model):
	user =models.OneToOneField(User)
	voteid = models.IntegerField(default = 0,verbose_name = u"是否投票")
	vote_time = models.DateTimeField(default = datetime.now() - timedelta(hours =24),verbose_name = u'最后投票时间')
	def __unicode__(self):
		return self.user.username

class Eventinfo(models.Model):
	ei_id = models.IntegerField(primary_key = True,default = 2,verbose_name = u'活动编号')
	ei_name = models.CharField(max_length = 100,verbose_name = u'活动名称')
	start_time = models.DateTimeField(verbose_name = u'开始时间')
	end_time = models.DateTimeField(verbose_name = u'结束时间')
	def __unicode(self):
		return self.ei_name

