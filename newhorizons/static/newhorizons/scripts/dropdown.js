$( document ).ready( function() { 
    if((navigator.userAgent.match(/iPhone/i)) || (navigator.userAgent.match(/iPod/i)) || (navigator.userAgent.match(/iPad/i))) {
        $("#main_navigation .tab").click(function(){ $(this).find(".dropdown ul").css("left", "auto") });
        $(document).click( function() { $(".dropdown ul").css("left", "-999em"); });
    }
});	