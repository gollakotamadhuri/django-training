from django.shortcuts import render

from .models import User


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
