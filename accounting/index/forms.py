# -*- coding: utf-8 -*-

from django import forms
# from captcha.fields import CaptchaField

class UserForm(forms.Form):
	"""用户登录表单"""
	username = forms.CharField(
					label = '用户名',
					max_length = 128,
					widget = forms.TextInput(
						attrs = {
							'class':'layui-input',
							'lay-verify':'required|username',
							'placeholder':'请输入用户名',
							'autocomplete':'off'
						}
					),
					error_messages = {'invalid': u'用户名错误'}
				)

	password = forms.CharField(
					label = '密码',
					max_length = 128,
					widget = forms.PasswordInput(
						attrs = {
							'class':'layui-input',
							'lay-verify':'required|password',
							'placeholder':'请输入密码',
							'autocomplete':'off'
						}
					),
					error_messages = {'invalid': u'密码错误'}
				)

	# captcha = CaptchaField(label = '验证码',)
