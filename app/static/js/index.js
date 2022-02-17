const validate = () =>{
    let targets = document.getElementById("messages");
    let buttons = document.getElementById("sendmessages");
    if (targets.value.trim() === ""){
        buttons.style.color = "black";
    }else{
        buttons.style.color = "#0F9DA6";
    }
}

const validateSend = () =>{
    let targets = document.getElementById("messages");
    if(targets.value.trim() === ""){
        return false;
    }
}

const closetab = () =>{
    document.getElementById("menuitems").style.display = "none";
    document.getElementById("open").style.display = "block";
    document.getElementById("close").style.display = "none";
}

const opentab = () =>{
    document.getElementById("menuitems").style.display = "block";
    document.getElementById("open").style.display = "none";
    document.getElementById("close").style.display = "block";
}

const ValidateSignups = () =>{
    var username = document.getElementById("saveusername").value.trim();
    var contact = document.getElementById("savecontact").value.trim();

    if(username === "" || contact === ""){
       if(username === ""){
           return false;
       }else{
           return false;
       }
    }
}