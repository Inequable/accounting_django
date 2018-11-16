# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from index.models import *
from index.forms import *

# Create your views here.
# 登录操作
def login(request):
	# 表单元素，需在前端渲染
	login_form = UserForm()
	# 判断是否登录，避免重复登录
	if request.session.get('is_login', None):
		return redirect('/index/index')
	# 未登录状态下的post表单提交事务
	if request.method == 'POST': #login.html是用POST方式提交，这里判断是POST方式后，就处理获取到的数据
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		code = request.POST.get('code', None)
		message = ''
		if username and password and code:
			username = username.strip()
			try:
				userInfo = user.objects.get(username=username)
				# 判断前端提交的密码和数据库的是否一致，以及验证码是否正确
				if (userInfo.password == password) and (request.session['verifycode'] == code):
					# 将登录成功的用户信息记录在session会话里
					request.session['is_login'] = True
					request.session['user_id'] = userInfo.id
					request.session['user_name'] = userInfo.username
					return redirect('/index/index')
				elif request.session['verifycode'] != code:
					message = '验证码输入错误'
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
	return render(request, 'login.html', locals())

# 登出操作
def logout(request):
	# 本身就处于未登录状态，就没必要登出，直接跳转到登录页
	if not request.session.get('is_login', None):
		return redirect('/index/login')
	# 清空所有的session会话
	request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
	return redirect('/index/login')

# 主页面
def main(request):
	if not request.session.get('is_login', None):
		return redirect('/index/login')
	return render(request, 'index.html')

def account(request):
	if not request.session.get('is_login', None):
		return redirect('/index/login')
	return render(request, 'accounting.html')

def bill(request):
	if not request.session.get('is_login', None):
		return redirect('/index/login')
	return render(request, 'bill.html')

def sortManagement(request):
	if not request.session.get('is_login', None):
		return redirect('/index/login')
	return render(request, 'sortManagement.html')

# 用户注册
def register(request):
	if not request.session.get('is_login', None):
		return redirect('/index/login')
	return render(request, 'register.html')