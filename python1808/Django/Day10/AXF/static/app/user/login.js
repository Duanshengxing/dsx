$(function () {

    $('#username,#password').focus(function () {
        $('#show_warning').text('');
    });

    flag1 = false;
    flag2 = false;
   $('#username').blur(function () {
       let user = $(this).val();
       if (/^[a-zA-Z_]\w{5,17}$/.test(user)){
           $('#user-tip').text('').css('color','');
           flag1 = true
       }
       else {
           $('#user-tip').text('用户名不合法').css('color','red');
           flag1 = false
       }
   });

   $('#password').blur(function () {
       let password = $(this).val();
       if (password){
           $('#password-tip').text('').css('color','');
           flag2 = true
       }
       else{
           $('#password-tip').text('密码不能为空').css('color','red');
           flag2 = false
       }
   });

   $('#login').click(function () {
       if (flag1 && flag2){
           $('#password').val(md5($('#password').val()))
       }
       else {
           return false
       }
   });




});