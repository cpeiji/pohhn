/**
 * Created by xiangyang on 2017/7/9.
 */
param = {type:1}
var data = ajax("/getRecord.json",param);
console.log(data);

var html = '<div class="mdl-grid">';

$.each(data,function (index,obj) {
  var isWatch = '';
    if(obj.is_click == 1){
      isWatch="已观看"
    }
    var card = '<div class="demo-card-wide mdl-card mdl-shadow--2dp" style="width: 100%;height:100%">' +
          '<div class="mdl-card__title" style="padding: 0px;">' +
          '<img src="'+obj.pic+'" width="100%"/>'+//--
          '</div>' +
          '<div class="mdl-card__supporting-text">' +
          obj.name +'</br><small>上传时间：'+obj.gmt_create+'</small>'+//--
          '</div>' +
          '<div class="mdl-card__actions mdl-card--border">' +
          '   <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect" target="_blank" href='+obj.link+' >' +
          '观看' +//--
          '   </a>' +
          '</div>' +
          '<div class="mdl-card__menu" style="color: red">' +
          isWatch+
          '</div>' +
        '</div>';
    var inner_html = '<div class="mdl-cell mdl-cell--3-col" style="padding: 10px">'+card+'</div>'
    html += inner_html;
});
html += '</div>';





var bilibili = new Vue({
  el: '#bilibili',
  data: {
    content: html
  }
})