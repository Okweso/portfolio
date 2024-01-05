function hideForm(){
    document.getElementById('form1').style.display='none';
    var messages = document.getElementsByClassName('Ok_message');
    for (var i = 0; i < messages.length; i++) {
        messages[i].style.display = 'none';
    }
}
window.onload = hideForm

window.onload = function pre_loader() {
    document.getElementById('btn1').style.display='none';

};

function buttn(){
    document.getElementById('form1').style.display='';
}
function message_sent(){
    var message = document.getElementsByClassName('Ok_message');
    for (var i = 0; i < message.length; i++) {
        message[i].style.display = '';
    }
    var bodyy = document.querySelectorAll('.email_btn');
    for (var i =0; i<bodyy.length; i++) {
        bodyy[i].style.filter='blur(3px)';
        bodyy[i].style.zIndex=1;
        
    }
    
   
    
}

function afterSent(){
    document.getElementById('btn3').onclick = function(){
        window.location.reload();
    }
}

function submitHandler(){
    message_sent();
    afterSent();
    
}
function sendSuccessful(){
    var emailData = {
         sender : document.forms["ContactForm"]["from_email"].value,
         subject : document.forms["ContactForm"]["subject"].value,
         message : document.forms["ContactForm"]["message"].value
    }
    $.ajax({
        url: '/contact/',
        method: 'POST',
        data: emailData,
        success: function(response){
            if (response.status === 'success'){
            alert("message sent successfully");


        }
            else {
                alert("message sending failed");
            }
            
        }
    });
}