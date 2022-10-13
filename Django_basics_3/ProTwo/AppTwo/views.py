from django.shortcuts import render

from AppTwo.forms import UserForm
from AppTwo.models import User


# Create your views here.
def help(request):
    my_dict = {'help_me': "Help Page"}
    return render(request, 'AppTwo/help.html', context=my_dict)


def index(request):
    my_dict = {'insert_data': "Thanks!"}
    return render(request, 'AppTwo/index.html', context=my_dict)


def user(request):
    user_info = User.objects.all()
    user_dict = {'user_data': user_info}
    return render(request, 'AppTwo/user.html', context=user_dict)

def signup(request):
    f = UserForm()

    if request.method == 'POST':
        f = UserForm(request.POST)

        if f.is_valid():
            f.save()
            print("Saved data is: ")
            print("FIRST NAME: ", f.cleaned_data['first_name'])
            print("LAST NAME: ", f.cleaned_data['last_name'])
            print("EMAIL: ", f.cleaned_data['email'])
            return user(request)
        else:
            print("Form data invalid!")
    
    return render(request, 'AppTwo/signup.html', context={'form':f})
