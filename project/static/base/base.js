$(document).ready(function () {

    $('.nav-link').click(function(){
        $(this).removeClass("waves-effect waves-light");
    });

    var top1 = $('#home').offset().top;
    var top2 = $('#features').offset().top;

});

$(document).scroll(function() {
    var scrollPos = $(document).scrollTop();
    alert(scrollPos);
    if (scrollPos >= top1 && scrollPos < top2) {
        alert('test');
        $('#change').css('background-color', '#f00');
    } else if (scrollPos >= top2) {
        alert('test2');
        $('#change').css('background-color', '#0f0');
    }
});