//由于模块都一次性加载，因此不用执行 layui.use() 来加载对应模块，直接使用即可：
;!function(){
	var layer = layui.layer,
	form = layui.form,
	$=layui.jquery;
	// layer.msg('Hello World');
	
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
		code:[/^[\S]{5}$/,'验证码必须5位，且不能出现空格']
	});
	
	//监听提交
	form.on('submit(sbt)', function(data){
	  // layer.msg(JSON.stringify(data.field));//会返回提交的信息
	  if (JSON.stringify(data.field)) {
	  	return true;
	  }
	  return false;
	});
// 、、、、、、、
	$('#regist').on('click',function () {
		
		layer.msg('这里应该弄一个注册的功能', {
	      time: 720000, //720s后自动关闭,12分钟
	      btn: ['注册', '取消'],
	      btnAlign: 'c',
	      yes:function (index,layero) {
	      	//按钮一的回调函数
	      	layer.msg('按钮一');
	      	layer.close(index);
	      },
	      btn2:function (index,layero) {
	      	//按钮二的回调函数
	      	layer.close(index);
	      }
	    });

	});
// 、、、、、、、
}();