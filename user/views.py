from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

from . models import Profile, Posts
from .forms import ProfileForm , Reguser, PostForm
from django.contrib import messages
from olxclone.views import hompage


from django.core.mail import send_mail
from django.conf import settings

def adduser(request):
    if request.method=='POST':
        form=Reguser(request.POST)
        if form.is_valid():
            a = form.save()
            subject = 'WELCOME MAIL'
            message = f' welcome {a.username} to our website '
            from_mail = settings.EMAIL_HOST_USER
            to = [a.email]

            send_mail(subject,message,from_mail,to)
            Profile.objects.create(user = a )
            messages.success(request,'User has been registered')
            return redirect(hompage)
    else:
        form = Reguser()
    return render(request,'register.html',{'form':form})




from django.contrib.auth import authenticate,login,logout
def loginpage(request):
    if request.method=='POST':
        usern= request.POST['user']
        passw= request.POST['pass']

        user=authenticate(request,username=usern,password=passw)
        if user:
            
            login(request,user)
            print('logged in')
            messages.success(request,'user is authenticated')
            return redirect(hompage)
        else:
            print('no such user')    

    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    messages.success(request,'user has been logged out')
    return redirect(hompage)


def adduser(request):
     if request.method=='POST':
          form=Reguser(request.POST)
          if form.is_valid():
               form.save()
               messages.success(request,'User has been registered')
               return redirect(hompage)
     else:
          form =Reguser()
     return render(request,'register.html',{'form':form})


def profilepage(request):

       pro, created = Profile.objects.get_or_create(user=request.user)
    
       return render(request, 'profile.html', {'pro': pro})


def editprofile(request,eid):
    
    pro = Profile.objects.get(id=eid)

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=pro)
        if form.is_valid():
            form.save()
            return redirect(profilepage)
    else:   
        form = ProfileForm(instance=pro)
    return render(request,'editprofile.html',{'form':form})

def addpost(request):
    if request.method =='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.user = request.user
            a.save()
            return redirect(hompage)
    else:    
        form = PostForm()
    return render(request,'addposts.html',{'form':form})
