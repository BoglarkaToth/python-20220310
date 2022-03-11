window.onload = () =>  {
    document.querySelector("#submit-button").onclick = () => { 
        let name = document.querySelector("#name-input").value;
        document.querySelector("#message-p").innerHTML = "Hello " + name + "!";
        // maradjon az oldalon, ne kommunikáljon szerverrel:
        return false;
    };
}