# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from index.models import *
from index.forms import *

# Create your views here.
def login(request):
	if request.method == 'POST': #login.html是用POST方式提交，这里判断是POST方式后，就处理获取到的数据
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		message = ''
		if username and password:
			username = username.strip()
			try:
				userInfo = user.objects.get(username=username)
				if userInfo.password == password:
					return redirect('/index/index')
				else:
					message = '密码错误'
			except:
				message = '查无此用户'
		'''
		这里使用了一个小技巧，Python内置了一个locals()函数，它返回当前所有的本地变量字典，
		我们可以偷懒的将这作为render函数的数据字典参数值，就不用费劲去构造一个形如{'message':message, 'login_form':login_form}的字典了。
		这样做的好处当然是大大方便了我们，但是同时也可能往模板传入了一些多余的变量数据，造成数据冗余降低效率。
		'''
		return render(request, 'login.html', locals())
	login_form = UserForm()
	return render(request, 'login.html', locals())

def main(request):
	return render(request, 'index.html')

def account(request):
	return render(request, 'accounting.html')

def bill(request):
	return render(request, 'bill.html')

def sortManagement(request):
	return render(request, 'sortManagement.html')