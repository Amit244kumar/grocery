function showhide(){
    var input=document.getElementsByClassName("forget")
    if(input[1].type=="password")
    {
        input[1].type="text"
        input[2].type="text"
    }
    else{
        input[1].type="password"
        input[2].type="password"
    }
}



var input=document.getElementsByClassName("forgetpwd")
function hide(){ 
  input[0].style.display="none"
}

function show(){
   
    input[0].style.display="block"
}



function sendData(){
    //document.getElementsByTagName("form").preventDefault();
    t=document.getElementById('msg')
    var obj=document.getElementsByClassName("forget") 
    if(obj[0].value == "" || obj[1].value== "" || obj[2].value == ""){
        return 
    }
    if(obj[1].value!=obj[2].value)
    {
        t.innerHTML="password is not same"
        t.id="error"
        return 
    }
    const dataToSend={
       email:obj[0].value,
       password:obj[1].value
    }
    // alert(dataToSend.name)
    // alert(dataToSend.email)
    // alert(dataToSend.number)
    // alert(dataToSend.comment)
    // Django server endpoint URL
    const apiUrl = 'http://localhost:8000/forgetPassword/';

    // Fetch options for a POST request
    const fetchOptions = {
        method: "POST",
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            // You may need additional headers like authentication tokens if required
        },
        body: JSON.stringify(dataToSend),
    };
   
    // Send data to the Django server using fetch and promises
    fetch(apiUrl, fetchOptions)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json(); // Assuming the server returns JSON data
        })
        .then(data => {
            if(data.status == 'success')
            {
                t.innerHTML=data.message
                t.id="changed"
                setTimeout(()=>{
                    document.getElementsByClassName("forgetpwd")[0].style.display="none"
                },2000)
            }
        })
        .catch(error => {
            // Handle errors during the fetch or server response
            console.error("Error sending data to Django server:", error);
        });
}



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}