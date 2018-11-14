layui.use(['table','element','form','laypage','layer'], function(){
  var table = layui.table,//表格
  element=layui.element,//元素操作
  form=layui.form,//表单
  laypage=layui.laypage,//分页
  layer=layui.layer,//弹窗
  $=layui.jquery;//jquery插件

  table.render({
    elem: '#colData',
    url:'testData/',
    cellMinWidth: 125, //全局定义常规单元格的最小宽度，layui 2.2.1 新增
    cols: [[
      {field:'Id', width:80, title: 'ID', sort: true},
      {field:'cols', title: '分类名称', edit:'text', align:'center'},
      {field:'cols_account', title: '收支分类', edit:'text', align:'center'},
      {field:'cols_info', title: '备注信息', edit:'text'},
      {field:'cols_date', title: '分类创建时间', align:'center'},
      {field:'cols_finallydate', title: '最后修改时间', align:'center'},
      {fixed: 'right', title:'操作', align:'center', toolbar: '#column'}
    ]],
    page: true
  });

  //监听工具条
  table.on('tool(colData)', function(obj){ //注：tool是工具条事件名，billData是table原始容器的属性 lay-filter="对应的值"
    var data = obj.data //获得当前行数据
    ,layEvent = obj.event; //获得 lay-event 对应的值
    if(layEvent === 'del'){
      layer.confirm('真的删除行么', function(index){
        obj.del(); //删除对应行（tr）的DOM结构
        layer.close(index);
        //向服务端发送删除指令
      });
    } else if(layEvent === 'colModify'){
      layer.msg('修改操作');
    }
  });

  //节点克隆,并清空节点内容
  $('#addCol').on('click',function () {
    //只clone第一个
    $(".col-node").append($(".col .site-block:first").clone(true));
    //重新渲染组件
    form.render('select');
    //清空表单的数据后clone
    $(':input','.col-node')  
    .not(':button, :submit, :reset, :hidden')  
    .val('')  
    .removeAttr('checked')  
    .removeAttr('selected');
    checkNode();
  });
  
  checkNode();//时刻检查
  //检查节点个数，判断是否让 删除节点按钮显示
  function checkNode() {
    if ($('.col-node .site-block').length<=0) {
      // console.log('asdjkhk');
      $('#delCol').hide();
    }else{
      // console.log($('.col-node .site-block').length);
      $('#delCol').show();
    }
  }
  
  //删除clone节点
  $('#delCol').on('click',function () {
    $(".col-node .site-block:last").remove();
    checkNode();
  });

});