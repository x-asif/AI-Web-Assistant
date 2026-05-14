async function sendMessage(){

    let input =
    document.getElementById("message");

    let message = input.value;

    if(message.trim() === ""){

        return;
    }

    let formData = new FormData();

    formData.append(
        "message",
        message
    );

    let response = await fetch(
        "/ask",
        {
            method:"POST",
            body:formData
        }
    );

    let data = await response.text();

    let chat =
    document.getElementById("chat");

    chat.innerHTML += `
        <div class="user">
            <b>You:</b> ${message}
        </div>
    `;

    chat.innerHTML += `
        <div class="bot">
            <b>Assistant:</b> ${data}
        </div>
    `;

    input.value = "";

    chat.scrollTop =
    chat.scrollHeight;
}



document
.getElementById("message")
.addEventListener(
    "keypress",
    function(event){

        if(event.key === "Enter"){

            sendMessage();
        }
    }
);



const micButton =
document.getElementById("mic-btn");


const recognition =
new webkitSpeechRecognition();


recognition.lang = "en-US";

recognition.continuous = false;


micButton.onclick = function(){

    recognition.start();

    micButton.innerHTML = "🎙️";
}


recognition.onresult = function(event){

    let transcript =
    event.results[0][0].transcript;

    document.getElementById(
        "message"
    ).value = transcript;

    micButton.innerHTML = "🎤";

    sendMessage();
}