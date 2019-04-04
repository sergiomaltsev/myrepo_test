$('document').ready(function () {
    $('input#id_title').on('click', function () {
        var title = $('input#id_title').val();
        console.log(title);

        $.ajax({
            url:"/hello/get_title/",
            data:{"title":title},
            success:function (data) {
                if (data == 'Error'){
                    console.log("Hello error");
                    $('input#id_title').css({'border-color':'red'})
                }
                else {
                    console.log('Hello world');
                    $('input#id_title').css({'border-color':'grey'})
                }
            }
        })
    });
});