
function setContent(url) {
    if (url.split(',')[1] == "admissions_counseling") {
        $.get(url.split(',')[0], function(data) {
            var $data = $(data);
            var len = $data.children().length
            $data.children().each(function(i,v){
                if (i != len-1) $(this).remove();
            });
            $data.children('li').children('h3').remove();
            $('#content').html($data);
        });
        return false;
    } else {
        $( "#content" ).load(url);
        return false;
    }
}

/*function setPartial (url, appendAfterEl) {
    $.get(url, function(data) {
        $('#content ' + appendAfterEl).siblings().remove();
        $('#content ' + appendAfterEl).after(data);
  });
}*/
$(document).on('click','a.from-blog-authors', function(e){
    e.preventDefault();
    var trimester = $('a.active').text();
    var year = $('a.active').parent().parent().parent().siblings('a').text();
    var url_part = '/blogs/'+year+'/';
    switch(trimester){
        case 'Oct-Nov-Dec':
            setContent(url_part+4);
        break;
        case 'Jul-Aug-Sep':
            setContent(url_part+3);
        break;
        case 'Apr-May-Jun':
            setContent(url_part+2);
        break;
        case 'Jan-Feb-Mar':
            setContent(url_part+1);
        break;
        default:
            setContent('/blogs');
        break;
    }
    return false;
});
    
function setNav(url) {
    $( "#secondary_navigation" ).load(url);
    return false;
}

function setHeader($content) {
    $( "#page_content_header" ).html($content);
    return false;
}

function setAdvert($content) {
    $( "#advert_space" ).load($content);
    return false;
}

function setActive(id) {
    $('a').removeClass('active');
    $(id).addClass('active');
    return false;
}
