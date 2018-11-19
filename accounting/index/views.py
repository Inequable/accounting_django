# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, HttpResponse
import json
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
				if (userInfo.password == encryption(password)) and (request.session['verifycode'] == code):
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


# 使用原生sql语句的网站参考网址：https://blog.csdn.net/u012422446/article/details/52623069
# 用户注册
# 中文字符转化未弄过，全部有中文字符的都要注意一下，后期更改
def register(request):
	if request.session.get('is_login', None):
		return redirect('/index/index')
	# 判断是否是异步请求
	if request.is_ajax() and request.method == 'POST':
		ret = {"code":"0", "msg":"", "count":"", "data":[]}
		# 处理前端获取的json数据
		data = json.loads(request.body.decode("utf8"))
		data['password'] = encryption(data['password'])
		# 唯一用户命验证
		if user.objects.filter(username=data['username']):
			ret['msg'],ret['code'] = '用户名已存在',-1
			return HttpResponse(json.dumps(ret))
		# 获取模型对象
		m_user = user()
		code = data.pop('code') # 删除code字段名，因为不属于user表内的字段，并取得该值
		if request.session['verifycode'] != code:
			ret['code'],ret['msg'] = -1,'注册失败，验证码错误'
		else:
			for key,value in data.items():
				field = user._meta.get_field(key) # 字段是否与模型表字段对应
				if value and field:
					setattr(m_user, key, value) # 有值并且对应上模型表的字段名，将模型对象的字段设置值
			# 插入数据
			m_user.save()
			if m_user.id: # 判断返回对象是否为空any()函数
				ret['msg'] = '注册成功'
		return HttpResponse(json.dumps(ret)) # 响应成对应的json格式（对应layui的json格式）
	# 不是异步重定向登录页面
	return redirect('/index/login')

# 加密-密码
import hashlib
def encryption(password=''):
	password = password + 'SALT'
	encryption_pass = hashlib.md5(password.encode('utf-8'))
	return encryption_pass.hexdigest()
