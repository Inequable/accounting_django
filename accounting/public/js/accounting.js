layui.use(['form', 'laydate'], function(){
  var laydate = layui.laydate //加载进laydate模块
  ,form = layui.form  //加载进form模块
  ,$ = layui.jquery;  //加载jquery
  
  //执行一个laydate实例，时间插件
  // laydate.render({
  //   elem: '.pay', //指定元素
  //   type:'datetime',//指定时间类型
  //   calendar: true, 
  // });//由于此版本的laydate控件无法多次clone使用，故放弃

  //监听提交，表单监听
  form.on('submit(sbt)', function(data){
    if (JSON.stringify(data.field)) {//如果有提交数据，允许跳转
      return true;
    }
    return false;
  });

  //检查节点个数，判断是否让 删除节点按钮显示
  function checkNode() {
    //支出节点
    if ($('.pay-node .site-block').length<=0) {
      // console.log('asdjkhk');
      $('#delPay').hide();
    }else{
      // console.log($('.pay-node .site-block').length);
      $('#delPay').show();
    }
    //收入节点
    if ($('.income-node .site-block').length<=0) {
      // console.log('asdjkhk');
      $('#delIncome').hide();
    }else{
      // console.log($('.income-node .site-block').length);
      $('#delIncome').show();
    }    
  }
  checkNode();

  //支出节点克隆 
  $('#addPay').on('click',function () {
    //只clone第一个
    $(".pay-node").append($(".pay .site-block:first").clone(true));
    //重新渲染组件
    form.render('select');
    //清空表单的数据后clone
    $(':input','.pay-node')  
    .not(':button, :submit, :reset, :hidden')  
    .val('')  
    .removeAttr('checked')  
    .removeAttr('selected');
    checkNode();
  });

  //收入节点克隆 
  $('#income').on('click',function () {
    //只clone第一个
    $(".income-node").append($(".income .site-block:first").clone(true));
    //重新渲染组件
    form.render('select');
    //清空表单的数据后clone
    $(':input','.income-node')  
    .not(':button, :submit, :reset, :hidden')  
    .val('')  
    .removeAttr('checked')  
    .removeAttr('selected');  
    checkNode();    
  });
 
    //删除clone节点
  $('#delPay').on('click',function () {
    $(".pay-node .site-block:last").remove();
    checkNode();
  });
    //删除clone节点
  $('#delIncome').on('click',function () {
    $(".income-node .site-block:last").remove();
    checkNode();
  });

});