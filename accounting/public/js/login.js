//由于模块都一次性加载，因此不用执行 layui.use() 来加载对应模块，直接使用即可：
;!function(){
	var element = layui.element,layer = layui.layer,form = layui.form,laytpl = layui.laytpl,$=layui.jquery;

	//自定义验证
	form.verify({
		username:function(value){
			if (value.length < 5) {
				return '用户名不符合长度！！！';
			}else if(/^\d+\d+\d$/.test(value)){
				return '用户名不能全为数字';
			}
		},
		password:[/^[\S]{6,12}$/,'密码必须6到12位，且不能出现空格'],
		code:[/^[\S]{5}$/,'验证码必须5位，且不能出现空格'],
		confirmPassword:function (value) {
			var pass = $('#password').val();
			if (!(new RegExp(pass)).test(value)) {
				return '再次输入密码错误';
			}
		},
	});

	//监听提交
	form.on('submit(sbt)', function(data){
		if (JSON.stringify(data.field)) {
			return true;
		}
		return false;
	});

	$('#regist').on('click',function () {
		laytpl($('#register').html()).render({
			// name: '贤心'
		}, function(html){
			layer.open({
				type:1,
				title: ['用户信息注册'],
				content:html,
				area: ['600px', '650px'],
				closeBtn: 0,
				anim: 5,
			})
		});
		form.render();
		form.on('submit(register)', function (_data) {
			console.log(_data.field);
			$.ajax({
				type: 'POST',
				url: '/index/register/',
				headers: {"X-CSRFToken":$("[name='csrfmiddlewaretoken']").val()}, // 要用请求头的ajax，伪造csrf验证
				contentType: 'application/json', // 提交json的数据
				data: JSON.stringify(_data.field), // 这里需要转化成json格式
				success: function (_res) {
					if (_res.code == '0') {
						layer.msg('注册成功', {
							icon: 6,
							time: 2000,
						});
						layer.closeAll();
					}else{
						layer.msg('注册失败', {
							icon: 5,
							time: 2000,
						});
					}
				}
			});
			return false;
		});
	});

	$(document).keyup(function (e) {
		var key = e.which;
		if (key === 27) {
			layer.closeAll();
		}
	});
}();