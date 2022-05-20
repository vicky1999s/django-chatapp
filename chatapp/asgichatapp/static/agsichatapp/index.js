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


const url = `ws://${window.location.host}/ws/socket-server`;
const chatSocket = new WebSocket(url);
chatSocket.onmessage = function(e){
    let data = JSON.parse(e.data);
    console.log(data);
    console.log(data["type"]);
    if (data["type"] === 'chat'){
        let msg = document.getElementById("messages");
        console.log(data["message"]);
        msg.insertAdjacentHTML('afterend', `<div><p>${data["message"]}</p></div>`);
    }
}

var form = document.getElementById("form");
form.addEventListener("submit", (e)=>{
    e.preventDefault();
    let msg = e.target.message.value;
    chatSocket.send(JSON.stringify(
        {"message":msg}
    ))
    form.reset();
})