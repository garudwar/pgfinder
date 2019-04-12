from django.shortcuts import render,redirect
from . models import ItemModel,RegisterModel
from .forms import LoginForm,RegisterForm,AddForm
import  json
from random import randint
import requests

# Create your views here.
type=None

def  homepage(request):
    q = request.GET.get("q")
    if q is not None:
        obj = ItemModel.objects.filter(title__contains=q)
    else:
        obj = ItemModel.objects.all()

    is_empty=len(obj)==0
    return  render(request,"home.html",{'data':obj,'is_empty':is_empty})

def  pgdetail(request):

    idd=request.GET.get("id")
    obj = ItemModel.objects.get(id=idd)

    return  render(request,"pgdetail.html",{'obj':obj})


def signup(request):
    u = request.POST.get("username")
    p = request.POST.get("password")
    e = request.POST.get("email")
    i = request.FILES.get("image")
    request.session["message"] = "welcome to Signup Page"

    if u is not None and p is not None and e is not None and i is not None:
        obj = RegisterModel(username=u, password=p, email=e, image=i)
        obj.save()
        request.session["message"] = " successfully registered"

    f = RegisterForm()

    return render(request, "signup.html", {'f': f})


def login(request):
    global type

    u = request.POST.get("username")
    p = request.POST.get("password")

    if u is not None and p is not None:

        row = RegisterModel.objects.filter(username=u, password=p)

        if (len(row) > 0):
            request.session["yes"] = "loggedin"
            request.session["username"] = row[0].username
            request.session["image"] = json.dumps(str(row[0].image).strip('"'))

    obj = LoginForm()

    return render(request, "login.html", {'f': obj})

def logout(request):
    del request.session["yes"]
    return redirect("http://localhost:8000/login")



def addpage(request):

    t=request.POST.get("title")
    d=request.POST.get("description")
    i=request.FILES.get("image")
    p=request.POST.get("price")
    b=request.POST.get("buildingtype")
    c=request.POST.get("contact")
    e=request.POST.get("email")
    l=request.POST.get("location")
    po=request.POST.get("postedon")
    ps=request.POST.get("postedby")
    

    request.session["message"]="Welcome to Add PG Page"
    if  t is  not None and d is not None and i is not None and p is not None and b is not None and c is not None and e is not None and l is not None and po is not None and ps is not None:
        
        obj=ItemModel(title=t,description=d,image1=i,price=p,buildingtype=b,contact=c,email=e,location=l,postedon=po,postedby=ps)
        obj.save()
        request.session["message"]=" Successfully Added"
        

    f=AddForm()
    return render(request,"add.html",{'f':f})

def  intro1(request):
    
    x=randint(1000, 9999)
    return  render(request,"intro1.html",{'otpvalue':x})


def  intro2(request):

    otpvalue=request.POST.get("otpvalue")
    number=request.POST.get("number")
    confirmotp= request.POST.get("confirm")
    request.session["msg"]="waiting for  otp"
    

    if otpvalue is not None and number is not None:
        url="http://control.msg91.com/api/sendotp.php?authkey=269653ADyir7WZvWV5c9c579b&message=your  otp is  "+otpvalue+"&sender=PGFind&mobile="+number+"&otp="+otpvalue
        res=requests.get(url)
        request.session["otpvalue"]=otpvalue


    if confirmotp is not None:
        if confirmotp == request.session["otpvalue"]:
            request.session["msg"]="success confirmed"
            return redirect("http://localhost:8000/signup/")
        else:
            request.session["msg"]="please enter valid otp"
        
    return render(request,"intro2.html",None)



