/**
 * Created by xiangyang on 2017/7/9.
 */
function ajax(url,data){
     var result;
     $.ajax({
         type: "GET",
         url: url,
         data: data,
         dataType: "json",
         async: false,
         success: function(s_data){
             // console.log(JSON.stringify(s_data));
             result = s_data
         },
         error:function (e_data) {
             result = e_data
         }
     });
     return result;
}
