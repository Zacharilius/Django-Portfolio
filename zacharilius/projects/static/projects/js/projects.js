$(document).ready(function(){
    $('#odd-job-desktop-button').click(function(){
        updateOddJobPicture('odd-job-desktop-pic');
    })

    $('#odd-job-tablet-button').click(function(){
        updateOddJobPicture('odd-job-tablet-pic');
    })

    $('#odd-job-mobile-button').click(function(){
        updateOddJobPicture('odd-job-mobile-pic');
    })

    function updateOddJobPicture(imageFileName){ 
        $('.odd-job-pic').hide()
        $('#' + imageFileName).show();
    }
})