from django.shortcuts import render,redirect
from django.contrib.auth.models import  User,auth
from django.contrib import messages,sessions
from .models import Posts,Profile,chatBoxed,score
import datetime
# Create your views here.
def sign(request):
    return render(request,'sign.html')

def register(request):
    if request.method == "POST":
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['username']
        password1=request.POST['password']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1 == password2 :
            if User.objects.filter(username=username).exists():
                print("username taken")
                messages.info(request,"Username Already Taken")
            else :
                user=  User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                user.save()
                print("Addded")
                user=auth.authenticate(username=username,password=password1)

                #request.session[username]=password1
                auth.login(request,user)
                
                return redirect('/corehome')
        else :
            messages.info(request,"Passwords did not match")
        return redirect('/')

def loginurl(request):
    return render(request,'login.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password']
        user=auth.authenticate(username=username,password=password1)
        if user is not None:
            auth.login(request,user)
            request.session[username]=password1
            return redirect('/corehome')
        else:
            messages.info(request,"Invaid Credentials")
    return redirect('/loginurl')

def corehome(request):
    data=Posts.objects.all()
  #  print(auth.get_username())
    return render(request,'files/corehome.html',{'posts':data})


def search(request):
    data=User.objects.order_by('-username').reverse()
    print(request.user)
    
    return render(request,'files/search.html',{'users':data})


def chatbox(request):
    data=chatBoxed.objects.order_by('-date').reverse()
    print('data',data)
    return render(request,'files/charbox.html',{'datas':data})
def profile(request):
    return render(request,'files/profile.html')
def insert(request):
    if request.method=='POST':
        c=chatBoxed()
        c.username=request.user
        c.texted=request.POST['text']
        c.date=datetime.datetime.now()
        c.save()
        c=chatBoxed.objects.all()
        print('inserted',c)

    return redirect('/chatbox')

def logout(request):
    auth.logout(request)
    return render(request,'sign.html')


def query(request):
    try:
        return render(request,'query.html')
    except:
        return render('/corehome')
def scoremy(request):
    if request.method =='POST':
        a=score()
        a.username=request.user
        a.myscore=request.POST['score']
        a.save()

    return redirect('/profile')
