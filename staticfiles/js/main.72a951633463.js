$(document).ready(function(){

    $('.input-group.date').hide()

    $('#id_checkbox_datetime').click(function(){
        var datetime = $('.input-group.date')
        if ($(this).is(":checked")) {
            datetime.show()
        } else {
            datetime.hide()
        }
    });


});
