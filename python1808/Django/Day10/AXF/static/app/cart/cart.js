$(function () {

   // +
    $('.add').click(function () {
        //获取要修改的商品id
        cartid = $(this).parents('li').attr('cartid');
        let that = this;
        $.post('/axf/cart_num_add/',{cartid:cartid},function (data) {
            let obj = data;
            if (obj.status == 1){
                $(that).prev().text(obj.num);
                calculateTotalPrice();

            }
            else {
                alert(obj.msg)
            }
        })


    });
 // -
    $('.reduce').click(function () {
        //获取要修改的商品id
        cartid = $(this).parents('li').attr('cartid');
        let that = this;
        $.post('/axf/cart_num_reduce/',{cartid:cartid},function (data) {
            let obj = data;
            if (obj.status == 1){
                $(that).next().text(obj.num);
                calculateTotalPrice();

            }
            else {
                alert(obj.msg);
            }
        });


    });

    //删除
    $('.delbtn').click(function () {
        let that = this;
        cartid = $(this).parent().attr('cartid');
        $.post('/axf/cart_goods_del/',{cartid:cartid},function (data) {
             let obj = data;
            if (obj.status == 1){
                $(that).parent().remove();
                checkselectall();

            }
            else {
                alert(obj.msg);
            }
        })
    });

    // 判断是否全选
    $('#select_all').click(function () {
        let that = this;
        let isAllSelect = $(this).find('span').html() ? 1 : 0;
        $.post('/axf/cart_select_all/',{isAllSelect:isAllSelect},function (data) {
            let obj = data;
            if (obj.status == 1){
                $('#select_all,.one_span').children().text(obj.selectall ? '√' : '')
                checkselectall()
            }
            else {
                alert(obj.msg)
            }

        });

    });

    //判断单选状态
    $('.one_span').click(function () {
         let that = this;
        cartid = $(this).parents('li').attr('cartid');
       if ($(this).children().text()){
           $(this).children().text('');

       }
       else {
           $(this).children().text('√')
       }
        span_status = $(this).children().text();
        $.post('/axf/select_status/',{cartid:cartid,span_status:span_status},function (data) {
            let obj = data;
            if (obj.status == 1){
                checkselectall()
            }
            else {
                alert(obj.msg)
            }
        })
    });

    checkselectall();
    //判断全选状态
    function checkselectall() {
        let flag = true;
        $('.one_span').each(function () {
            let gou = $(this).find('span').html();
            flag = flag && Boolean(gou)

        });

        if (flag){
            $('#select_all').find('span').html('√');
        }
        else {
            $('#select_all').find('span').html('');
        }
        calculateTotalPrice();
    }






    //计算商品总价
    function calculateTotalPrice() {
        let total = 0;
        $('.one_span').each(function () {
           let gou = $(this).find('span').html();
           if (gou){
               let price = $(this).parents('li').find('.price').text();
               let num = $(this).parents('li').find('.num').text();
               total += parseFloat(price)*parseInt(num);
           }
        });
        $('#total').text(total.toFixed(2)) //保留两位小数
    }

});


