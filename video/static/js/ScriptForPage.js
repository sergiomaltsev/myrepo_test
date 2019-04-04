$('document').ready(function () {
    $('.like').on('click', function () {
        var id = $(this).attr('id');
        console.log(id);
        $.ajax({
            url:"/hello/addlike/",
            data:{'id':id},
            success:function (data) {
                console.log(data)
                if(id[0]=='l'){$('h3#' + id).html('likes ' + data)}
                else{$('h3#like' + id).html('likes ' + data)}

            }
        });
    });

    $('input#comment').on('click',function () {
        var slug = $('input#slug').attr('value');
        var text = $('textarea').val();
        console.log(text);
        $.ajax({
            url:"/hello/addcomm/",
            data:{'slug':slug, 'comment':text},
            success:function (data) {
                $('div#comments').append('<h1>' + text + '</h1>');
            }
        });
        console.log(slug)
    })
});