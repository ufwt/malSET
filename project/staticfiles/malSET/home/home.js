function uploadFile() {
    var fn = $('#file_upload').val();
    var filename = fn.match(/[^\\/]*$/)[0]; // remove C:\fakename
    console.log(filename);
    $('#inputFile').submit();
    console.log($('#inputFile'));
}

$(document).ready(function () {
    $('#file_upload').on("change", function(){ uploadFile(); });
});


$(document).scroll(function() {
    var $window = $(window);
    var windowsize = $window.width();
    if (windowsize > 991) {
        var scrollPos = $(document).scrollTop();

        var top1 = $('#home').offset().top;
        var top2 = $('#features').offset().top;

        if (scrollPos < top2) {
            $('.navbar').css('background-color', 'rgba(0,0,0,0)');
        } else if (scrollPos >= top2) {
            $('.navbar').css('background-color', '#00498D');
        }
    }
    else {
        $('.navbar').css('background-color', '#00498D');
    }
});