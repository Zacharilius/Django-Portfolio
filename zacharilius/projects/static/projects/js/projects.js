$(document).ready(function(){
    $('#odd-job-desktop-button').click(function(){
        updateOddJobPicture(this, 'odd-job-desktop-pic');
    })
    
    $('#odd-job-tablet-button').click(function(){
        updateOddJobPicture(this, 'odd-job-tablet-pic');
    })
    
    $('#odd-job-mobile-button').click(function(){
        updateOddJobPicture(this, 'odd-job-mobile-pic');
    })
    
    function updateOddJobPicture(clickedSelector, imageFileName){ 
        $('.zws-screen').removeClass('is-active');
        $(clickedSelector).addClass('is-active');
    
        $('.odd-job-pic').hide();
        $('#' + imageFileName).fadeIn();
    }
})