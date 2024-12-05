from django.shortcuts import render
from .models import Register,History
import razorpay
import re
from datetime import datetime
from django.conf import settings
from django.contrib.auth.hashers import make_password,check_password
def home(request):
    return render(request,"onlinepayment/home.html")
def profile(request,email):
        o=Register.objects.filter(Email=email)
        amt=History.objects.filter(Email=email)
        collection=0
        for i in amt:
                    if i.Status=="Successfully":
                       collection+=int(float(i.Amount))
        if(len(o)>0):
               return render(request,"onlinepayment/profile.html",{"user":o[0],"collection":collection})
def register(request):
    return render(request,"onlinepayment/register.html")
def signup(request):
    if request.method=="POST":
        name=request.POST.get("name")
        mobile=request.POST.get("mob")
        passs=request.POST.get("pass")
        email=request.POST.get("email")
        Address=request.POST.get("add")
        ch=Register.objects.filter(Email=email)
        if(len(ch)==0):
         if len(passs) < 8:
            return render(request,"onlinepayment/home.html",{"error":"Password must be at least 8 characters long."})
         if not re.search(r"[A-Z]", passs):
            return render(request,"onlinepayment/home.html",{"error":"Password must contain at least one uppercase letter."})
            
         if not re.search(r"[a-z]", passs):
            return render(request,"onlinepayment/home.html",{"error":"Password must contain at least one Lowercase letter."})

         if not re.search(r"\d", passs):
            return render(request,"onlinepayment/home.html",{"error":"Password must contain at least one digit."})

         if not re.search(r"[@$!%*?&#]", passs):
                return render(request,"onlinepayment/home.html",{"error":"Password must contain at least one special character."})
            
         passs=make_password(passs)
         o=Register(Name=name,Email=email,Password=passs,Mobile=mobile,Address=Address) 
         o.save()
         return render(request,"onlinepayment/home.html",{"error":"Successfull Added"})
        else:
            return render(request,"onlinepayment/home.html",{"error":"Email Already Exist"})

def signin(request):
    if request.method=="POST":
        passs=request.POST.get("pass")
        email=request.POST.get("email")
        o=Register.objects.filter(Email=email)
        amt=History.objects.filter(Email=email)
        collection=0
        for i in amt:
                    if i.Status=="Successfully":
                       collection+=int(float(i.Amount))
        if(len(o)>0):
            if(check_password(passs,o[0].Password)):
               return render(request,"onlinepayment/profile.html",{"user":o[0],"collection":collection})
            else:
                return render(request,"onlinepayment/home.html",{"error":"password not matched"})
        else:
                return render(request,"onlinepayment/home.html",{"error":"email not matched"})
def payment(request):
  if request.method=="POST":
    amt=request.POST.get("amt")
    amt=int(amt)*100
    id=request.POST.get("email")
    o=Register.objects.filter(Email=id)
    client=razorpay.Client(auth=(settings.KEY,settings.SECRET))
    payment=client.order.create({"amount":amt,"currency":"INR","payment_capture":1})
    amt=History.objects.filter(Email=id)
    collection=0
    for i in amt:
                    if i.Status=="Successfully":
                       collection+=int(float(i.Amount))
    return render(request,"onlinepayment/payment.html",{"payment":payment,"user":o[0],"collection":collection})
def editprofile(request,):
    if request.method=="POST":
        name=request.POST.get("name")
        mobile=request.POST.get("mob")
        passs=request.POST.get("pass")
        email=request.POST.get("email")
        Address=request.POST.get("add")
        passs=make_password(passs)
        o=Register.objects.filter(Email=email).update(Name=name,Email=email,Password=passs,Mobile=mobile,Address=Address)
        return render(request,"onlinepayment/home.html")
def donepayment(request,id):
    a=id.split("{}")
    h=datetime.now().hour
    m=datetime.now().minute
    s=datetime.now().second
    mo=datetime.now().month
    year=datetime.now().year
    dat=datetime.now().day
    datee=f"{dat}/{mo}/{year}"
    time=f"{h}/{m}/{s}"
    p=History(Orderid=a[0],Amount=str(int(a[1])/100),Time=time,Date=datee,Email=a[2],Status="Successfully")
    p.save()
    o=Register.objects.filter(Email=a[2])
    amt=History.objects.filter(Email=a[2])
    collection=0
    for i in amt:
        if i.Status=="Successfully":
                       collection+=int(float(i.Amount))
    return render(request,"onlinepayment/profile.html",{"user":o[0],"status":"Payement is Successfully","collection":collection})

def cancelpayment(request,id):
    a=id.split("{}")
    h=datetime.now().hour
    m=datetime.now().minute
    s=datetime.now().second
    mo=datetime.now().month
    year=datetime.now().year
    dat=datetime.now().day
    datee=f"{dat}/{mo}/{year}"
    time=f"{h}/{m}/{s}"
    p=History(Orderid=a[0],Amount=str(int(a[1])/100),Time=time,Date=datee,Email=a[2],Status="Cancelled")
    p.save()
    o=Register.objects.filter(Email=a[2])
    amt=History.objects.filter(Email=a[2])
    collection=0
    for i in amt:
         if i.Status=="Successfully":
                       collection+=int(float(i.Amount))
    return render(request,"onlinepayment/profile.html",{"user":o[0],"status":"payment is cancelled","collection":collection})

def history(request,id):
    o=History.objects.filter(Email=id)
    print(o)
    return render(request,"onlinepayment/history.html",{"his":[o],"user":id})
