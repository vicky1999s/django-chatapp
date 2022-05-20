function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

$(function(){
    $("#sendBtn").bind('click', function(){
        const csrftoken = Cookies.get('csrftoken');
        let msg = document.getElementById("msg").value;
        let postUrl = "send_message";
        if (msg=="quit")
            postUrl = "logout" 
        console.log(msg);
            $.ajax({
                url : postUrl,
                type: "POST", 
                data: {"msg":msg},
                headers: { 'X-CSRFToken': csrftoken },
                success: function(data, response, jqXHR) {
                    console.log(data);
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.log(jqXHR);
                      console.log(textStatus);
                      console.log(errorThrown);
                }
            });

        return false;
    });
   });

function validate(name){
    if(name.length > 3)
        return true
    return false
}