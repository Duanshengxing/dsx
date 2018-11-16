$(function () {


    //前段做本地校验
    flag1 = false;
    flag2 = false;
    flag3 = false;
    flag4 = false;
    //检测用户名
    $('#username').blur(function () {
       var value = $(this).val();
       if (/^[a-zA-Z_]\w{5,17}$/.test(value)) {
           $('#user-tip').text('').css('color','green');
           flag1 = true;
       }
       else{
           $('#user-tip').text('用户名不合法').css('color','red');
           flag1 = false;
       }
    });

    //检测密码
     $('#password').blur(function () {
       var value = $(this).val();
       if (/^\w{8,16}$/.test(value)) {
           $('#password-tip').text('').css('color','green');
           flag2 = true;

       }
       else{
           $('#password-tip').text('密码不合法').css('color','red');
           flag2 = false;

       }
    });

     //检测确认密码
    $('#repassword').blur(function () {
        var pwd = $('#password').val();
       var value = $(this).val();
       if (value == pwd) {
           $('#repassword-tip').text('').css('color','red');
           flag3 = true;

       }
       else {
           $('#repassword-tip').text('两次密码不一样').css('color','red');
           flag3 = false;

       }
    });



    //检测邮箱
     $('#email').blur(function () {
       var value = $(this).val();
       if (/^\w+@\w+(\.\w+)+$/.test(value)) {
           $('#email-tip').text('邮箱合法').css('color','green');
           flag4 = true;
       }
       else{
           $('#email-tip').text('邮箱不合法').css('color','red');
           flag4 = false;
       }
    });

     //注册
    $('#register').click(function () {
        if (flag1 && flag2 && flag3 && flag4){
            //提交表单之前加密
            $('#password').val(md5($('#password').val()))
        }else {
            return false;
        }

    })
});