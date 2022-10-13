from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import UserInfoForm, UserProfileForm


# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(redirect_to=reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in!")


def register(request):
    
    user_form = UserInfoForm()
    profile_form = UserProfileForm()
    registered = False
    if request.method == 'POST':
        user_form = UserInfoForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
            return HttpResponseRedirect(redirect_to=reverse('basic_app:userlogin'))
        else:
            print(user_form.errors,profile_form.errors)

    return render(request, "basic_app/register.html", {'register': registered,
                                                       'user_form': user_form,'profile_form':profile_form})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username , password = password)

        if user:

            if user.is_active:

                login(request, user)
                return HttpResponseRedirect(redirect_to=reverse("index"))

            else:
                return HttpResponse("USER NOT ACTIVE") 
        
        else:

            print("Someone tired to login to the website")
            print("Username used :{} , Password used: {} ".format(username,password))

            return HttpResponse("Incorrect details")
    
    else:
        return render(request,"basic_app/userlogin.html",{})
