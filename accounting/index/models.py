# -*- coding: UTF-8 -*-
# 任何中文注释都需要将上面那句放在表头

from django.db import models

# you can see...https://docs.djangoproject.com/zh-hans/2.1/ref/models/fields/
# Create your models here.
class bill(models.Model):
	"""创建一个account表"""
	# 默认自动生成带有主键的id
	# 类里面的字段代表数据表中的字段(name)，数据类型则由CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度。
	userId = models.IntegerField(default=0, verbose_name='用户名id')
	money = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='金额(元/￥)')
	TYPE_CHOICES = (
		('1', '收入'),
		('2', '支出'),
	)
	billType = models.CharField(max_length=4, choices=TYPE_CHOICES, default='1', verbose_name='收支，默认1为收入2为支出')
	colsId = models.IntegerField(default=0, verbose_name='收支类型id')
	mark = models.TextField(null=True, blank=True, default='', verbose_name='文本备注')
	time = models.DateField(default='', verbose_name='收支时间')
	finallydate = models.DateTimeField(auto_now=True, verbose_name='最后一次更改这笔账单的时间')
	isdel = models.SmallIntegerField(default=0, verbose_name='是否删除，默认0未删除1是删除')


class classify(models.Model):
	"""创建一个classify表"""
	adate = models.DateTimeField(auto_now_add=True, verbose_name='添加时，追加当前添加时间')
	userId = models.IntegerField(default=0, verbose_name='用户名id')
	name = models.CharField(max_length=50, verbose_name='类目名称')
	TYPE_CHOICES = (
		('1', '收入'),
		('2', '支出'),
	)
	billType = models.CharField(max_length=4, choices=TYPE_CHOICES, default='1', verbose_name='收支，默认1为收入2为支出')
	mark = models.TextField(null=True, blank=True, verbose_name='文本备注')
	finallydate = models.DateTimeField(auto_now=True, verbose_name='最后一次更改的时间')
	isdel = models.SmallIntegerField(default=0, verbose_name='是否删除，默认0未删除1是删除')


class log(models.Model):
	"""导出日志"""
	adate = models.DateTimeField(auto_now_add=True, verbose_name='添加时，追加当前添加时间')
	ip = models.CharField(max_length=255, verbose_name='记录导出的ip服务端与客户端的ip，用 ~ 分割')
	condition = models.CharField(max_length=100, verbose_name='导出的条件，是以那个条件导出数据的')
	userId = models.IntegerField(default=0, verbose_name='用户名id')
	isdel = models.SmallIntegerField(default=0, verbose_name='是否删除，默认0未删除1是删除')


class user(models.Model):
	"""用户表user"""
	adate = models.DateTimeField(auto_now_add=True, verbose_name='添加时，追加当前添加时间/注册时间')
	username = models.CharField(max_length=100, verbose_name='用户名称/账号')
	password = models.CharField(max_length=100, verbose_name='用户密码')
	SEX_CHOICES = (
		('1', '男'),
		('2', '女'),
	)
	sex = models.CharField(null=True, blank=True, max_length=4, verbose_name='性别，默认1为男2为女')
	addr = models.CharField(null=True, blank=True, default='', max_length=255, verbose_name='地址')
	email = models.EmailField(null=True, blank=True, max_length=254, default='', verbose_name='邮箱')
	wechat = models.CharField(null=True, blank=True, max_length=100, default='', verbose_name='微信号')
	qq = models.CharField(null=True, blank=True, max_length=100, default='', verbose_name='qq号')
	vip = models.SmallIntegerField(default=0, verbose_name='vip等级')
	GROUP_CHOICES = (
		('1', '学生'),
		('2', '农民'),
		('3', '白领'),
		('4', 'Boss'),
		('5', '职工'),
	)
	group = models.CharField(max_length=4, default=1, choices=GROUP_CHOICES, verbose_name='用户组')
	isdel = models.SmallIntegerField(default=0, verbose_name='是否删除，默认0未删除1是删除')
