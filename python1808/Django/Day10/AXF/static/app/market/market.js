$(function () {

    $('#all_type').click(function () {
        $('#show_all').slideToggle();
        $('#all_type_icon').toggleClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
    });
    $('#sort_type').click(function () {
        $('#sort_all').slideToggle();
        $('#sort_type_icon').toggleClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
    });
});


$('.add').click(function () {
   let numNode = $(this).prev();
   numNode.text(parseInt(numNode.text())+1);
});

$('.reduce').click(function () {
   let numNode = $(this).next();
   if (parseInt(numNode.text())>1){
       numNode.text(parseInt(numNode.text())-1);
   }

});


$('.addtocart').click(function () {
    let num = $(this).prev().find('.num').text();
    let goodsid = $(this).attr('goodsid');



   $.get('/axf/cart_add/',{goodsid:goodsid,num:num},function (data) {
       let obj = data;
       if (obj.status == 1){
            alert('加入购物车成功')
        }
        else{
            if (obj.status == 0){
                let res = confirm('您尚未登录，是否前往登录');
                if (res){
                    location.href = '/axf/login/'
                }
            }
            else {
                alert(obj.msg)
            }
       }
   }) ;
});