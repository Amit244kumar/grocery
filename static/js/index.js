var toggleVariable=0;
//0 means dropdown list is close and 1 means open
function toggle(){
    var element=document.getElementById("dropdown")
    if(toggleVariable == 0)
    {
        toggleVariable=1;
        element.style.display="block"; 
    }
    else{
        toggleVariable=0
        element.style.display="none"; 
    }
}
document.getElementsByClassName

var preScrollpos=window.pageYOffset

window.onscroll=function(){
    var curScrollpos=window.pageYOffset
    if(preScrollpos > curScrollpos)
    {
        document.getElementById("scrolling-header").style.top="0px"
    }
    else
    {
        document.getElementById("scrolling-header").style.top="-232px"
    }
    preScrollpos=curScrollpos
}

function addToCartOpen()
{
    document.getElementById("add-to-cart").style.left="1152px";
    document.getElementById("body").style.overflow="hidden"
}

function addToCartClose()
{
    document.getElementById("add-to-cart").style.left="1528px";
    document.getElementById("body").style.overflow="scroll"
}




function addingProductToCart(img,n)
{
    if(!document.getElementById("email").innerHTML){
        return 
    }
    for(i=img-1;i<=img+3;i++)
    {
        if(document.getElementsByClassName("img")[i].style.display == "block")
        {
            img=i;
            break;
        }
    }
    
    // Sample data to send to the server

    arr=String(document.getElementsByClassName("product-price")[n].innerText)
    const dataToSend = {
        email:document.getElementById("email").innerHTML,
        ProductName:  document.getElementsByClassName("name")[n].innerHTML,
        price: arr.split(" ")[0],
       
        imageName:String(document.getElementsByClassName("img")[img].getAttribute("src")).split("/")[3],
        quantity:1,
    };

    // Django server endpoint URL
    const apiUrl = "http://localhost:8000/addProductToCart/";

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
            // document.getElementById("add-to-cart").style.left="1152px";
            // document.getElementById("body").style.overflow="hidden"
            console.log("Response from Django server:", data.status);
            let product=document.getElementById('added-product')
            if(data.status == "error")
            {
                product.innerHTML=data.message
                product.style.display="block"
                
            }
            else{
                product.innerHTML="product added to cart sucessfully"
                product.style.display="block"
            }
            setTimeout(function(){
                product.style.display="none"
              },10000)
        })
        .catch(error => {
            // Handle errors during the fetch or server response
            console.error("Error sending data to Django server:", error.message);
        });
}

function deleteProduct(img){
    const dataToSend={
        email:document.getElementById("email").innerHTML,
        imageName:String(document.getElementsByClassName("image")[img-1].getAttribute("src")).split("/")[3],
    }

    // Django server endpoint URL
    const apiUrl = "http://localhost:8000/deleteProduct/";

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
            // document.getElementById("add-to-cart").style.left="1152px";
            // document.getElementById("body").style.overflow="hidden"
            console.log("Response from Django server:", data.status);
            let product=document.getElementById('added-product')
            if(data.status == 'success')
            {
                product.innerHTML="product deleted successfully"
                product.style.display="block"

            }
            setTimeout(function(){
                product.style.display="none"
            },10000)
            var p=document.getElementsByClassName("product-content")
            p[img-1].style.display="none"
            
        })
        .catch(error => {
            // Handle errors during the fetch or server response
            console.error("Error sending data to Django server:", error);
        });
}











// Function to get the CSRF token from cookies
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

var val=document.getElementsByClassName("val")
var price=document.getElementsByClassName("pr")

var totalPrice=document.getElementsByClassName("totalPrice")

function decrement(n){  
    n--;
    if(Number(val[n].innerHTML)!=0)
    {
        val[n].innerText=Number(val[n].innerHTML)-1;
        totalPrice[0].innerHTML=(Number(totalPrice[0].innerHTML)-Number(price[n].innerHTML)).toFixed(1)
    }
    else{
        totalPrice[0].innerHTM=0;
    }
}

function increment(n){
    n--
    val[n].innerText=Number(val[n].innerHTML)+1;
    totalPrice[0].innerHTML=(Number(totalPrice[0].innerHTML)+Number(price[n].innerHTML)).toFixed(1)
}

window.onload = function () {
    total = 0;
    // Assuming 'price' is a NodeList or HTMLCollection
    var priceArray = Array.from(price);

    priceArray.forEach(element => {
        total += Number(element.innerHTML);
    });
      
    totalPrice[0].innerHTML =  total.toFixed(1);
};

