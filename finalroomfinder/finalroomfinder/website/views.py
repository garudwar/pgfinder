from django.shortcuts import render,redirect
from . models import ItemModel,RegisterModel
from .forms import LoginForm,RegisterForm
import  json

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



