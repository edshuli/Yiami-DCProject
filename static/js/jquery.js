$(document).ready(function(){
    var myNav = $(".navbar");

    $(window).on('scroll', function() {
    "use strict";
    if ($(window).scrollTop() >= 100) {
        myNav.addClass("scroll");
    }
    else {
        myNav.removeClass("scroll");
    }
    });




});

