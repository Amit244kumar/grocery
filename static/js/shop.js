function addToCart(){
    let request=new XMLHttpRequest()
    let url='http://localhost:8000/addTocart/'
    request.open('GET',url,true)
    request.send()
    request.onreadystatechange=function(){
        if(request.readyState==4 && request.status == 200){
            if(request.responseText == 'True')
            {
              
            }else{

            }
        }
    }
}
