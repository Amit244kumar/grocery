document.getElementById("submit").addEventListener("click",()=>{
    //   document.getElementsByTagName("form").preventDefault();
       var obj=document.getElementsByClassName("input")   
 
    const dataToSend={
       name:obj[0].value,
       email:obj[1].value,
       number:obj[2].value,
       comment:document.getElementById("cmt").value
    }
    // alert(dataToSend.name)
    // alert(dataToSend.email)
    // alert(dataToSend.number)
    // alert(dataToSend.comment)
    // Django server endpoint URL
    const apiUrl = 'http://localhost:8000/quary/';

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
                document.getElementsByTagName("form").reset()
            }
        })
        .catch(error => {
            // Handle errors during the fetch or server response
            console.error("Error sending data to Django server:", error);
        });
})



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