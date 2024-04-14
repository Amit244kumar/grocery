from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from GR.models import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
"""
super user
username:amit123
password:amit12345
email:xyz@gmail.com
"""
def index(request):
    try:    
        if request.session['emailId']:
            products=addToCarProducts.objects.filter(user_Accounts=request.session['emailId'])
            i=1
            return render(request,'index.html',{'items':products})
    except KeyError:
        return render(request,'index.html')

def shop(request):
    try:    
        if request.session['emailId']:
            products=addToCarProducts.objects.filter(user_Accounts=request.session['emailId'])
            return render(request,'shop.html',{'items':products})
    except KeyError:
        return render(request,'shop.html')

#checking is user login and adding item to addToCart
def addToCart(request):
    try:
        if request.session['emailid']:
            return True
    except KeyError:
        return False


def about(request):
    try:    
        if request.session['emailId']:
            products=addToCarProducts.objects.filter(user_Accounts=request.session['emailId'])
            return render(request,'about.html',{'items':products})
    except KeyError:
        return render(request,'about.html')

#rendering login page
def login(request):
    msg=dict()
    try: 
        if request.GET['message']:
            msg['m']=" ".join(request.GET['message'].split("+"))
            return render(request,"login.html",{'msg':msg})
    except KeyError: 
        pass
    try: 
         if request.GET['login-error']:
            msg['error']=" ".join(request.GET['login-error'].split("+"))
            return render(request,"login.html",{'msg':msg})
    except KeyError:
        pass
    # try:    
    #     if request.session['emailId']:
    #         products=addToCarProducts.objects.filter(user_Accounts=request.session['emailId'])
    #         return render(request,'login.html',{'items':products})
    # except KeyError:
    #     pass     

    return render(request,'login.html')

def validating_user(request):
    if request.method == 'POST':
        if userAccounts.objects.filter(emailId=request.POST['email-id']):
            if userAccounts.objects.filter(emailId=request.POST['email-id'],password=request.POST['password']):
               userObject=userAccounts.objects.get(emailId=request.POST['email-id'])
               request.session['emailId']=userObject.emailId
               request.session['password']=userObject.password
               request.session['name']=userObject.firstName+" "+userObject.lastName
               products=addToCarProducts.objects.filter(user_Accounts=request.session['emailId'])
               return render(request,'index.html',{'items':products})
            else:
                return HttpResponseRedirect('http://localhost:8000/login?login-error=password+is+not+incorret')
        else:
            return HttpResponseRedirect('http://localhost:8000/login?login-error=email+is+not+incorret')
    else:
        return HttpResponseRedirect('http://localhost:8000/login/')

def sign_up(request):
    try:
        if request.GET['error']:
            error=dict()
            error['errorMessage']=" ".join(request.GET['error'].split("+"))
            return render(request,'sign_up.html',{"er":error})
    except KeyError:
        pass
    return render(request,'sign_up.html')


def wishlist(request):
    try:    
        if request.session['emailId']:
            products=addToCarProducts.objects.filter(user_Accounts=request.session['emailId'])
            return render(request,'wishlist.html',{'items':products})
    except KeyError:
        return render(request,'wishlist.html')


#Creating user account and saving their crediantials
def createAccount(request):
    if request.method == "POST":
        if not userAccounts.objects.filter(emailId=request.POST['email-id']):
            ua=userAccounts()
            ua.firstName=request.POST['first-name']
            ua.lastName=request.POST['last-name']
            ua.emailId=request.POST['email-id']
            ua.password=request.POST['password']
            ua.save()
            #print(ua.firstName,ua.lastName,ua.emailId,ua.password)
            return HttpResponseRedirect("http://localhost:8000/login?message=Account+created+succeessfully") 
        else:
            return HttpResponseRedirect("http://localhost:8000/sign_up?error=email+already+register")
    else:
        return HttpResponseRedirect("http://localhost:8000/")
    
    
def profile(request):
    try:    
        if request.session['emailId']:
            products=addToCarProducts.objects.filter(user_Accounts=request.session['emailId'])
            return render(request,'profile.html',{'items':products})
    except KeyError:
        return render(request,'profile.html')

#logouting user from his account
def logout(request):
    request.session.clear()
    return HttpResponseRedirect("http://localhost:8000/")

def contact(request):
    try:    
        if request.session['emailId']:
            products=addToCarProducts.objects.filter(user_Accounts=request.session['emailId'])
            return render(request,'contact.html',{'items':products})
    except KeyError:
        return render(request,'contact.html')

def add_product_to_cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            if addToCarProducts.objects.filter(imageName=data['imageName'],user_Accounts=data['email']).exists():  
                return JsonResponse({'status': 'error', 'message': 'product is already added to cart'})
            # print(type(eval(str(data['price']).split("$")[1])))
            user=userAccounts.objects.get(emailId=data['email'])
            product=addToCarProducts.objects.create(
                name=data['ProductName'],
                price=eval(str(data['price']).split("$")[1]),
                quantity=data['quantity'],
                imageName=data['imageName'],
                user_Accounts=user
            )
            product.save()
            # Process the data as needed
            # Example: Save the data to a model
            # YourModel.objects.create(**data)
            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)
    

def delete_product(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
           
            user_account = userAccounts.objects.get(emailId=data['email'])
            product = addToCarProducts.objects.get(imageName=data['imageName'],user_Accounts=user_account)
            product.delete()
            # Process the data as needed
            # Example: Save the data to a model
            # YourModel.objects.create(**data)
            return JsonResponse({'status': 'success','message': 'product deleted successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)

def quary(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            obj=userQuary.objects.get(emailId=data['email'])
            if not obj:
                qry=userQuary.objects.create(
                    name=data['name'],
                    emailId=data['email'],
                    number=data['number'],
                    comment=data['comment']
                )
            else:
                obj.comment=data['comment']
                obj.save()
            return JsonResponse({'status': 'success','message': ''})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)


def forgetPassword(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            # print(data)
            user=userAccounts.objects.get(emailId=data['email'])
            user.password=data['password']
            user.save()
            return JsonResponse({'status': 'success','message': 'change succefully'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)
 