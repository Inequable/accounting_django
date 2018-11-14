layui.use(['element','form','table'], function(){
  var $ = layui.jquery,
  element = layui.element,
  form=layui.form,
  table=layui.table;

  element.tab({
    headerElem: '.site-demo-nav>li', //指定tab头元素项
    bodyElem: '.layui-body>.layui-tab-item' //指定tab主体元素项
  });

  table.render({
    elem: '#billExport',
    // height: 315,
    url: '/kl', //数据接口
    page: true, //开启分页
    cols: [[ //表头
      {field: 'id', title: 'ID', width:80, sort: true, fixed: 'center'},
      {field: '', title: '导出时间段'},
      {field: '', title: '导出路径'},
      {field: '', title: '导出时间'} 
    ]]
  }); 

});