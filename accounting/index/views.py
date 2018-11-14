# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
def login(request):
	print(request.method)
	if request.method == 'POST': #login.html是用POST方式提交，这里判断是POST方式后，就处理获取到的数据
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		# 这个authenticate不能用，因为用的表是不一样的，django默认模块的表，与这个项目的情况不符
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect(reverse('index:index'))
		else:
			return render(request, 'login.html', {
				'username': username,
				'password': password,
			})
	return render(request, 'login.html')

@login_required(login_url = '/index/login')
def main(request):
	return render(request, 'index.html')

@login_required(login_url = '/index/login')
def account(request):
	return render(request, 'accounting.html')

@login_required(login_url = '/index/login')
def bill(request):
	return render(request, 'bill.html')

@login_required(login_url = '/index/login')
def sortManagement(request):
	return render(request, 'sortManagement.html')