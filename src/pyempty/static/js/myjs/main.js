$(function(){
    $.get('/current_time', function(data){
        $('.current_time').html(data);
    });
});
