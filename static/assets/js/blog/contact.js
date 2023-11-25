
$(document).ready(function(){
    //class on change functionaolity
    // register start here
    $("#contact_button").click(function (e) { 
    e.preventDefault();
    var user_message = $('#id_message').val();
        $.ajax({
            url: "/contact/",
            type: "POST",
            data: {
                name:$("input[name='name']").val(),
                phone_number:$("input[name='phone_number']").val(),
                email: $("input[name='email']").val(),
                subject: $("input[name='subject']").val(),
                message: user_message,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            },
            
            success: function (data) {
                console.log(data);
                if(data.status == "success"){
                    $('#success-message').text(data.message);
                    $('#contact-form')[0].reset();
                    // window.location.href = "/landing";
                }
                else{
                    alert(data.status);
                }
            }
        });


    });

    // register end here



});//main end
