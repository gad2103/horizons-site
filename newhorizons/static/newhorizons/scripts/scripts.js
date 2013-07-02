
function setContent(url) {
    $( "#content" ).load(url);
    return false;
}

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