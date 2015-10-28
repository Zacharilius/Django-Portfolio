$(document).ready(function(){
    console.log('ready');
    $('.mdl-navigation__link').click(function(){
        console.log('click');
        $('.mdl-navigation__link').removeClass('is-active');
        $(this).addClass('is-active');
    });
})